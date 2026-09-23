#!/usr/bin/env python3
"""Run matched-message and engagement/uptake analyses.

Expected input:
research_workspace/05_data/processed/communication_master_coded_v1.csv

Outputs are descriptive by design because social observability is partial.
"""

from pathlib import Path
import pandas as pd
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "research_workspace" / "05_data" / "processed" / "communication_master_coded_v1.csv"
OUT = ROOT / "research_workspace" / "07_analysis" / "outputs"
OUT.mkdir(parents=True, exist_ok=True)

EMOTIONS = [
    "fear_intensity","anxiety_uncertainty_intensity","anger_intensity","moral_outrage_intensity",
    "grief_sadness_intensity","solidarity_intensity","care_compassion_intensity","empathy_intensity",
    "hope_intensity","gratitude_intensity","pride_intensity","reassurance_intensity",
    "defiance_intensity","urgency_emotion_intensity"
]


def numeric(df, cols):
    for c in cols:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors="coerce")


def matched_message_summary(df: pd.DataFrame) -> pd.DataFrame:
    if "matched_message_id" not in df.columns:
        return pd.DataFrame()
    m = df[df["matched_message_id"].astype(str).ne("")].copy()
    if "match_confidence" in m.columns:
        m = m[m["match_confidence"].isin(["high", "medium", ""])]
    if m.empty:
        return m

    rows = []
    for mmid, g in m.groupby("matched_message_id"):
        website = g[g["platform_family"] == "website"]
        social = g[g["platform_family"] == "social"]
        row = {
            "matched_message_id": mmid,
            "organization": " | ".join(sorted(set(g.get("organization", "").astype(str)))) if "organization" in g else "",
            "n_items": len(g),
            "n_website": len(website),
            "n_social": len(social),
            "platforms": " | ".join(sorted(set(g.get("platform", "").astype(str)))),
            "match_confidence": " | ".join(sorted(set(g.get("match_confidence", "").astype(str)))) if "match_confidence" in g else "",
        }
        for c in EMOTIONS + ["urgency_level"]:
            if c in g.columns:
                row[f"website_{c}_mean"] = pd.to_numeric(website[c], errors="coerce").mean() if len(website) else np.nan
                row[f"social_{c}_mean"] = pd.to_numeric(social[c], errors="coerce").mean() if len(social) else np.nan
                row[f"social_minus_website_{c}"] = row[f"social_{c}_mean"] - row[f"website_{c}_mean"] if pd.notna(row[f"social_{c}_mean"]) and pd.notna(row[f"website_{c}_mean"]) else np.nan
        rows.append(row)
    return pd.DataFrame(rows)


def engagement_summary(df: pd.DataFrame) -> pd.DataFrame:
    metrics = ["like_or_reaction_count","comment_count","share_or_repost_count","view_count","observed_recirculation_minimum"]
    rows = []
    for metric in metrics:
        if metric not in df.columns:
            continue
        s = pd.to_numeric(df[metric], errors="coerce")
        observed = df[s.notna()].copy()
        if observed.empty:
            continue
        observed[metric] = pd.to_numeric(observed[metric], errors="coerce")
        for group_name, group in [("all_observed", observed)]:
            rows.append({
                "metric": metric,
                "group": group_name,
                "n_observed_items": len(group),
                "mean": group[metric].mean(),
                "median": group[metric].median(),
                "min": group[metric].min(),
                "max": group[metric].max(),
            })
        if "platform" in observed.columns:
            for platform, g in observed.groupby("platform"):
                rows.append({
                    "metric": metric,
                    "group": f"platform:{platform}",
                    "n_observed_items": len(g),
                    "mean": g[metric].mean(),
                    "median": g[metric].median(),
                    "min": g[metric].min(),
                    "max": g[metric].max(),
                })
    return pd.DataFrame(rows)


def uptake_summary(df: pd.DataFrame) -> pd.DataFrame:
    cols = [c for c in df.columns if c.startswith("uptake_") and c.endswith("_count")]
    if not cols:
        return pd.DataFrame()
    rows = []
    for c in cols:
        s = pd.to_numeric(df[c], errors="coerce")
        rows.append({
            "uptake_type": c,
            "items_with_observed_value": int(s.notna().sum()),
            "total_visible_instances": float(s.sum(skipna=True)),
            "items_with_at_least_one": int((s > 0).sum()),
        })
    return pd.DataFrame(rows)


def conversion_cases(df: pd.DataFrame) -> pd.DataFrame:
    if "conversion_signal_present" not in df.columns:
        return pd.DataFrame()
    flag = pd.to_numeric(df["conversion_signal_present"], errors="coerce")
    keep_cols = [c for c in [
        "item_id","org_id","organization","date","platform","title_or_caption","source_summary",
        "conversion_type","conversion_evidence_level","visible_interaction_rows",
        "matched_message_id","url"
    ] if c in df.columns]
    return df.loc[flag.eq(1), keep_cols].copy()


def main():
    df = pd.read_csv(DATA, dtype=str, keep_default_na=False)
    numeric(df, EMOTIONS + [
        "urgency_level","like_or_reaction_count","comment_count","share_or_repost_count","view_count",
        "observed_recirculation_minimum","visible_interaction_rows","conversion_signal_present"
    ])

    matched_message_summary(df).to_csv(OUT / "table_matched_message_differences.csv", index=False)
    engagement_summary(df).to_csv(OUT / "table_engagement_observed_only.csv", index=False)
    uptake_summary(df).to_csv(OUT / "table_public_uptake_summary.csv", index=False)
    conversion_cases(df).to_csv(OUT / "table_affective_conversion_cases.csv", index=False)
    print(f"Matched-message and engagement outputs written to {OUT}")


if __name__ == "__main__":
    main()
