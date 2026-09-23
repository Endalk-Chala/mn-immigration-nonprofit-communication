#!/usr/bin/env python3
"""Run core descriptive and temporal analyses for the affective intermediation study.

Expected input:
research_workspace/05_data/processed/communication_master_coded_v1.csv

Outputs:
research_workspace/07_analysis/outputs/

This script intentionally avoids treating hidden engagement as zero and supports
organization-normalized temporal estimates.
"""

from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "research_workspace" / "05_data" / "processed" / "communication_master_coded_v1.csv"
OUT = ROOT / "research_workspace" / "07_analysis" / "outputs"
OUT.mkdir(parents=True, exist_ok=True)

EMOTIONS = [
    "fear_intensity",
    "anxiety_uncertainty_intensity",
    "anger_intensity",
    "moral_outrage_intensity",
    "grief_sadness_intensity",
    "solidarity_intensity",
    "care_compassion_intensity",
    "empathy_intensity",
    "hope_intensity",
    "gratitude_intensity",
    "pride_intensity",
    "reassurance_intensity",
    "defiance_intensity",
    "urgency_emotion_intensity",
    "other_emotion_intensity",
]

APPRAISALS = [
    "threat_appraisal",
    "harm_loss_appraisal",
    "injustice_appraisal",
    "uncertainty_appraisal",
    "responsibility_blame_appraisal",
    "intentionality_appraisal",
    "norm_violation_appraisal",
    "vulnerability_appraisal",
    "controllability_appraisal",
    "coping_efficacy_appraisal",
    "collective_efficacy_appraisal",
    "care_need_appraisal",
    "opportunity_hope_appraisal",
]

FUNCTIONS = [
    "function_inform",
    "function_warn",
    "function_reassure",
    "function_regulate_fear",
    "function_mobilize",
    "function_advocate",
    "function_provide_service",
    "function_fundraise",
    "function_build_solidarity",
    "function_generate_empathy",
    "function_moral_evaluation",
    "function_increase_efficacy",
    "function_mourn_commemorate",
    "function_document_testify",
    "function_celebrate",
    "function_encourage_defiance",
    "function_other",
]


def to_num(df: pd.DataFrame, cols: list[str]) -> None:
    for c in cols:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors="coerce")


def corpus_summary(df: pd.DataFrame) -> pd.DataFrame:
    rows = [
        ("items", len(df)),
        ("organizations", df["org_id"].nunique() if "org_id" in df else np.nan),
        ("website_items", int((df.get("platform_family", "") == "website").sum())),
        ("social_items", int((df.get("platform_family", "") == "social").sum())),
        ("day_precision_items", int((df.get("date_precision", "") == "day").sum())),
    ]
    return pd.DataFrame(rows, columns=["metric", "value"])


def emotion_summary(df: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for c in EMOTIONS:
        if c not in df.columns:
            continue
        s = pd.to_numeric(df[c], errors="coerce")
        present = s >= 1
        rows.append({
            "emotion": c,
            "n_coded": int(s.notna().sum()),
            "prevalence_present": float(present.mean()) if len(s) else np.nan,
            "mean_intensity_all": float(s.mean()),
            "mean_intensity_when_present": float(s[present].mean()) if present.any() else np.nan,
            "n_intensity_0": int((s == 0).sum()),
            "n_intensity_1": int((s == 1).sum()),
            "n_intensity_2": int((s == 2).sum()),
            "n_intensity_3": int((s == 3).sum()),
        })
    return pd.DataFrame(rows)


def binary_summary(df: pd.DataFrame, cols: list[str], label: str) -> pd.DataFrame:
    rows = []
    for c in cols:
        if c not in df.columns:
            continue
        s = pd.to_numeric(df[c], errors="coerce")
        rows.append({
            "variable": c,
            "family": label,
            "n_coded": int(s.notna().sum()),
            "n_present": int((s == 1).sum()),
            "prevalence": float((s == 1).mean()),
        })
    return pd.DataFrame(rows)


def add_derived_emotion_measures(df: pd.DataFrame) -> pd.DataFrame:
    cols = [c for c in EMOTIONS if c in df.columns]
    if not cols:
        return df
    x = df[cols].apply(pd.to_numeric, errors="coerce")
    df = df.copy()
    df["overall_emotion_mean"] = x.mean(axis=1, skipna=True)
    df["overall_emotion_max"] = x.max(axis=1, skipna=True)
    df["overall_emotion_sum"] = x.sum(axis=1, skipna=True, min_count=1)
    df["emotional_repertoire_count"] = (x >= 1).sum(axis=1)
    return df


def weekly_emotional_arc(df: pd.DataFrame) -> pd.DataFrame:
    d = df.copy()
    d["date_parsed"] = pd.to_datetime(d.get("date", ""), errors="coerce")
    d = d[(d.get("date_precision", "") == "day") & d["date_parsed"].notna()].copy()
    d["week_start"] = d["date_parsed"] - pd.to_timedelta(d["date_parsed"].dt.weekday, unit="D")

    item_week = d.groupby("week_start", as_index=False).agg(
        item_count=("item_id", "count"),
        organization_count=("org_id", "nunique"),
        mean_emotion=("overall_emotion_mean", "mean"),
        median_emotion=("overall_emotion_mean", "median"),
    )

    org_week = (
        d.groupby(["week_start", "org_id"], as_index=False)
         .agg(org_week_mean_emotion=("overall_emotion_mean", "mean"))
    )
    norm = (
        org_week.groupby("week_start", as_index=False)
        .agg(org_normalized_mean_emotion=("org_week_mean_emotion", "mean"))
    )
    return item_week.merge(norm, on="week_start", how="left")


def role_summary(df: pd.DataFrame) -> pd.DataFrame:
    if "org_role_primary" not in df.columns:
        return pd.DataFrame()
    return (
        df.groupby("org_role_primary", dropna=False, as_index=False)
          .agg(
              item_count=("item_id", "count"),
              organization_count=("org_id", "nunique"),
              mean_emotion=("overall_emotion_mean", "mean"),
              mean_repertoire=("emotional_repertoire_count", "mean"),
          )
          .sort_values("item_count", ascending=False)
    )


def platform_summary(df: pd.DataFrame) -> pd.DataFrame:
    group = "platform_family" if "platform_family" in df.columns else "platform"
    return (
        df.groupby(group, dropna=False, as_index=False)
          .agg(
              item_count=("item_id", "count"),
              organization_count=("org_id", "nunique"),
              mean_emotion=("overall_emotion_mean", "mean"),
              mean_repertoire=("emotional_repertoire_count", "mean"),
          )
    )


def engagement_observability(df: pd.DataFrame) -> pd.DataFrame:
    metrics = ["like_or_reaction_count", "comment_count", "share_or_repost_count", "view_count"]
    rows = []
    for m in metrics:
        if m not in df.columns:
            continue
        s = pd.to_numeric(df[m], errors="coerce")
        rows.append({
            "metric": m,
            "items_metric_observed": int(s.notna().sum()),
            "items_total": len(df),
            "coverage": float(s.notna().mean()),
            "mean_when_observed": float(s.mean()),
            "median_when_observed": float(s.median()),
        })
    return pd.DataFrame(rows)


def plot_weekly_arc(weekly: pd.DataFrame) -> None:
    if weekly.empty:
        return
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(weekly["week_start"], weekly["mean_emotion"], marker="o", label="Item-weighted mean")
    ax.plot(weekly["week_start"], weekly["org_normalized_mean_emotion"], marker="o", label="Organization-normalized mean")
    ax.set_xlabel("Week")
    ax.set_ylabel("Mean emotion intensity")
    ax.set_title("Weekly emotional arc")
    ax.tick_params(axis="x", rotation=45)
    ax.legend()
    fig.tight_layout()
    fig.savefig(OUT / "figure_weekly_emotional_arc.png", dpi=200)
    plt.close(fig)


def main() -> None:
    df = pd.read_csv(DATA, dtype=str, keep_default_na=False)
    to_num(df, EMOTIONS + APPRAISALS + FUNCTIONS)
    df = add_derived_emotion_measures(df)

    corpus_summary(df).to_csv(OUT / "table_corpus_summary.csv", index=False)
    emotion_summary(df).to_csv(OUT / "table_emotion_summary.csv", index=False)
    pd.concat([
        binary_summary(df, APPRAISALS, "appraisal"),
        binary_summary(df, FUNCTIONS, "function"),
    ], ignore_index=True).to_csv(OUT / "table_appraisal_function_summary.csv", index=False)

    weekly = weekly_emotional_arc(df)
    weekly.to_csv(OUT / "table_weekly_emotional_arc.csv", index=False)
    role_summary(df).to_csv(OUT / "table_role_summary.csv", index=False)
    platform_summary(df).to_csv(OUT / "table_platform_summary.csv", index=False)
    engagement_observability(df).to_csv(OUT / "table_engagement_observability.csv", index=False)
    plot_weekly_arc(weekly)

    # Save enriched coded master with derived measures for downstream scripts.
    df.to_csv(OUT / "communication_master_coded_with_derived_v1.csv", index=False)
    print(f"Core analysis outputs written to {OUT}")


if __name__ == "__main__":
    main()
