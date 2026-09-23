#!/usr/bin/env python3
"""Prepare a coding sheet from the primary corpus and merge completed coding back.

Modes:
  prepare  -> creates research_workspace/05_data/processed/manual_coding_sheet_v1.csv
  merge    -> merges completed coding sheet into communication_master_primary_v1.csv
              and writes communication_master_coded_v1.csv

Usage:
  python research_workspace/07_analysis/prepare_and_merge_coding.py prepare
  python research_workspace/07_analysis/prepare_and_merge_coding.py merge
"""

from pathlib import Path
import sys
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
PROCESSED = ROOT / "research_workspace" / "05_data" / "processed"
MASTER = PROCESSED / "communication_master_primary_v1.csv"
CODING = PROCESSED / "manual_coding_sheet_v1.csv"
CODED_MASTER = PROCESSED / "communication_master_coded_v1.csv"

CODING_FIELDS = [
    "org_role_primary","org_role_secondary","role_hybrid_flag",
    "threat_appraisal","harm_loss_appraisal","injustice_appraisal","uncertainty_appraisal",
    "responsibility_blame_appraisal","intentionality_appraisal","norm_violation_appraisal",
    "vulnerability_appraisal","controllability_appraisal","coping_efficacy_appraisal",
    "collective_efficacy_appraisal","care_need_appraisal","opportunity_hope_appraisal",
    "fear_intensity","anxiety_uncertainty_intensity","anger_intensity","moral_outrage_intensity",
    "grief_sadness_intensity","solidarity_intensity","care_compassion_intensity","empathy_intensity",
    "hope_intensity","gratitude_intensity","pride_intensity","reassurance_intensity",
    "defiance_intensity","urgency_emotion_intensity","other_emotion_intensity",
    "emotion_explicitness","emotion_source_org","emotion_source_affected_public",
    "emotion_source_supporters_public","emotion_source_quoted_actor",
    "function_inform","function_warn","function_reassure","function_regulate_fear",
    "function_mobilize","function_advocate","function_provide_service","function_fundraise",
    "function_build_solidarity","function_generate_empathy","function_moral_evaluation",
    "function_increase_efficacy","function_mourn_commemorate","function_document_testify",
    "function_celebrate","function_encourage_defiance","function_other",
    "action_orientation_present","action_type","action_specificity","action_immediacy",
    "audience_primary","direct_address","urgency_level","legal_information_present",
    "service_information_present","resource_link_present","appraisal_notes","emotion_notes",
    "coder_id","coding_date","coder_confidence"
]

CONTEXT_FIELDS = [
    "item_id","org_id","organization","date","platform","platform_family","content_type",
    "title_or_caption","source_summary","url","language","media_type","analysis_inclusion_status",
    "sampling_status","unit_of_analysis_note","matched_message_id","match_confidence"
]


def prepare() -> None:
    df = pd.read_csv(MASTER, dtype=str, keep_default_na=False)
    out = pd.DataFrame()
    for c in CONTEXT_FIELDS:
        out[c] = df[c] if c in df.columns else ""
    for c in CODING_FIELDS:
        out[c] = ""
    out.to_csv(CODING, index=False)
    print(f"Prepared coding sheet with {len(out)} rows: {CODING}")


def merge() -> None:
    master = pd.read_csv(MASTER, dtype=str, keep_default_na=False)
    coding = pd.read_csv(CODING, dtype=str, keep_default_na=False)
    if coding["item_id"].duplicated().any():
        dupes = coding.loc[coding["item_id"].duplicated(), "item_id"].tolist()
        raise SystemExit(f"Duplicate item_id values in coding sheet: {dupes[:10]}")

    keep = ["item_id"] + [c for c in CODING_FIELDS if c in coding.columns]
    coded = master.merge(coding[keep], on="item_id", how="left", validate="one_to_one")
    coded.to_csv(CODED_MASTER, index=False)
    print(f"Merged coding into {len(coded)} primary rows: {CODED_MASTER}")


if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in {"prepare", "merge"}:
        raise SystemExit("Usage: prepare_and_merge_coding.py [prepare|merge]")
    prepare() if sys.argv[1] == "prepare" else merge()
