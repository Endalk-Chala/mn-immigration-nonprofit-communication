#!/usr/bin/env python3
"""Validate the coded analysis dataset before substantive analysis."""

from pathlib import Path
import sys
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "research_workspace" / "05_data" / "processed" / "communication_master_coded_v1.csv"

EMOTION_COLS = [
    "fear_intensity","anxiety_uncertainty_intensity","anger_intensity","moral_outrage_intensity",
    "grief_sadness_intensity","solidarity_intensity","care_compassion_intensity","empathy_intensity",
    "hope_intensity","gratitude_intensity","pride_intensity","reassurance_intensity",
    "defiance_intensity","urgency_emotion_intensity","other_emotion_intensity"
]

BINARY_PREFIXES = ("function_",)
BINARY_EXACT = [
    "role_hybrid_flag","threat_appraisal","harm_loss_appraisal","injustice_appraisal",
    "uncertainty_appraisal","responsibility_blame_appraisal","intentionality_appraisal",
    "norm_violation_appraisal","vulnerability_appraisal","controllability_appraisal",
    "coping_efficacy_appraisal","collective_efficacy_appraisal","care_need_appraisal",
    "opportunity_hope_appraisal","emotion_source_org","emotion_source_affected_public",
    "emotion_source_supporters_public","emotion_source_quoted_actor","action_orientation_present",
    "direct_address","legal_information_present","service_information_present","resource_link_present",
    "conversion_signal_present"
]

ALLOWED = {
    "emotion_explicitness": {"", "none", "implicit", "explicit", "mixed"},
    "action_specificity": {"", "none", "general", "specific"},
    "action_immediacy": {"", "none", "low", "moderate", "high"},
    "coder_confidence": {"", "low", "medium", "high"},
    "analysis_inclusion_status": {"include", "program_level_only", "exclude_from_primary_analysis", "duplicate_alias"},
}


def values_outside(series, allowed):
    vals = set(series.fillna("").astype(str).str.strip().unique())
    return sorted(vals - set(allowed))


def main():
    if not DATA.exists():
        raise SystemExit(f"Missing coded dataset: {DATA}")
    df = pd.read_csv(DATA, dtype=str, keep_default_na=False)
    errors = []
    warnings = []

    for required in ["item_id","org_id","organization","date","platform","analysis_inclusion_status"]:
        if required not in df.columns:
            errors.append(f"Missing required column: {required}")

    if "item_id" in df.columns:
        blank_ids = int(df["item_id"].astype(str).str.strip().eq("").sum())
        if blank_ids:
            errors.append(f"Blank item_id rows: {blank_ids}")
        dupes = df[df["item_id"].duplicated(keep=False)]["item_id"].unique().tolist()
        if dupes:
            errors.append(f"Duplicate item_id values: {dupes[:20]}")

    for c in EMOTION_COLS:
        if c not in df.columns:
            warnings.append(f"Emotion column absent: {c}")
            continue
        bad = values_outside(df[c], {"", "0", "1", "2", "3"})
        if bad:
            errors.append(f"{c} has illegal values: {bad}")

    binary_cols = set(BINARY_EXACT) | {c for c in df.columns if c.startswith(BINARY_PREFIXES)}
    for c in sorted(binary_cols):
        if c not in df.columns:
            continue
        bad = values_outside(df[c], {"", "0", "1"})
        if bad:
            errors.append(f"{c} has illegal binary values: {bad}")

    for c, allowed in ALLOWED.items():
        if c in df.columns:
            bad = values_outside(df[c], allowed)
            if bad:
                errors.append(f"{c} has illegal values: {bad}")

    if "urgency_level" in df.columns:
        bad = values_outside(df["urgency_level"], {"", "0", "1", "2", "3"})
        if bad:
            errors.append(f"urgency_level has illegal values: {bad}")

    # Engagement safeguard: explicitly unavailable/hidden metrics should not be mechanically encoded as zero.
    if "engagement_retrieval_status" in df.columns:
        hidden = df["engagement_retrieval_status"].astype(str).str.lower().str.contains("unavailable|hidden|not_exposed|not_visible", regex=True)
        for metric in ["like_or_reaction_count","comment_count","share_or_repost_count","view_count"]:
            if metric in df.columns:
                suspicious = hidden & df[metric].astype(str).str.strip().eq("0")
                if suspicious.any():
                    warnings.append(f"{metric}: {int(suspicious.sum())} unavailable/hidden rows encoded as 0; inspect manually.")

    if "date_precision" in df.columns and "week_start" in df.columns:
        bad_week = ~df["date_precision"].eq("day") & df["week_start"].astype(str).str.strip().ne("")
        if bad_week.any():
            warnings.append(f"{int(bad_week.sum())} non-day-precision rows have week_start values; weekly analysis should exclude them.")

    print("VALIDATION SUMMARY")
    print(f"Rows: {len(df)}")
    print(f"Organizations: {df['org_id'].nunique() if 'org_id' in df else 'NA'}")
    print(f"Errors: {len(errors)}")
    for e in errors:
        print(f"ERROR: {e}")
    print(f"Warnings: {len(warnings)}")
    for w in warnings:
        print(f"WARNING: {w}")

    if errors:
        sys.exit(1)


if __name__ == "__main__":
    main()
