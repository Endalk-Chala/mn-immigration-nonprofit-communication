#!/usr/bin/env python3
"""Select a stratified reliability-pilot sample from the primary master dataset.

Run after build_analysis_ready_dataset.py.
"""

from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
PROCESSED = ROOT / "research_workspace" / "05_data" / "processed"
MASTER = PROCESSED / "communication_master_primary_v1.csv"
OUT = PROCESSED / "reliability_pilot_sample_v1.csv"

RANDOM_SEED = 20260922
TARGET_N = 40


def main() -> None:
    df = pd.read_csv(MASTER, dtype=str, keep_default_na=False)
    if df.empty:
        raise SystemExit("Primary master dataset is empty.")

    rng = np.random.default_rng(RANDOM_SEED)
    df = df.copy()
    df["_rand"] = rng.random(len(df))

    # Ensure month/platform fields exist.
    if "month" not in df.columns:
        df["month"] = pd.to_datetime(df.get("date", ""), errors="coerce").dt.strftime("%Y-%m")
    if "platform_family" not in df.columns:
        df["platform_family"] = df.get("platform", "").map(lambda x: "website" if str(x).lower() == "website" else "social")

    # Prevent one organization from dominating the pilot: first draw at most one item per org/platform/month cell.
    cells = (
        df.sort_values("_rand")
          .groupby(["org_id", "platform_family", "month"], dropna=False, as_index=False)
          .head(1)
          .copy()
    )

    selected = []
    target_by_platform = {"website": TARGET_N // 2, "social": TARGET_N // 2}
    for platform_family, n in target_by_platform.items():
        pool = cells[cells["platform_family"] == platform_family].sort_values("_rand")
        selected.append(pool.head(n))

    pilot = pd.concat(selected, ignore_index=True).drop_duplicates("item_id")

    # Fill shortage from remaining items, prioritizing underrepresented months/orgs.
    if len(pilot) < TARGET_N:
        remaining = cells[~cells["item_id"].isin(pilot["item_id"])].copy()
        month_counts = pilot["month"].value_counts().to_dict()
        remaining["_month_count"] = remaining["month"].map(month_counts).fillna(0)
        remaining = remaining.sort_values(["_month_count", "_rand"])
        pilot = pd.concat([pilot, remaining.head(TARGET_N - len(pilot))], ignore_index=True)

    # Still short? Fill from all remaining verified rows.
    if len(pilot) < TARGET_N:
        remaining_all = df[~df["item_id"].isin(pilot["item_id"])].sort_values("_rand")
        pilot = pd.concat([pilot, remaining_all.head(TARGET_N - len(pilot))], ignore_index=True)

    pilot = pilot.head(TARGET_N).copy()
    pilot["pilot_order"] = rng.permutation(np.arange(1, len(pilot) + 1))
    pilot = pilot.sort_values("pilot_order")

    keep = [c for c in [
        "pilot_order", "item_id", "org_id", "organization", "date", "month", "platform",
        "platform_family", "content_type", "title_or_caption", "source_summary", "url",
        "analysis_inclusion_status", "sampling_status"
    ] if c in pilot.columns]
    pilot[keep].to_csv(OUT, index=False)
    print(f"Wrote {len(pilot)} pilot items to {OUT}")
    print(pilot["platform_family"].value_counts(dropna=False).to_string())
    print(pilot["month"].value_counts(dropna=False).sort_index().to_string())


if __name__ == "__main__":
    main()
