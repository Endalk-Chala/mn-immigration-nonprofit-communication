# Website Census Reconciliation — 2026-09-22

## Scope

Core sampling-frame reconciliation for TC001–TC084, study window 2025-11-01 through 2026-03-31.

## Substantive collection status

All core TC001–TC084 entities are now substantively accounted for in the website phase through one of the following outcomes:

1. verified exact-dated website items collected in raw CSV files;
2. partial/archive-limited status documented where no defensibly enumerable study-window archive could be recovered;
3. legacy/entity duplicate resolution; or
4. program-level attribution rules documented where the sampled entity is a program within a broader organization.

TC023 Missions Inc. Programs was the final substantive website-audit gap and was closed on 2026-09-22 with five verified exact-dated study-window items.

TC083 Navigate MN is treated as a legacy/duplicate identity of Unidos MN and is not collected as a separate corpus.

## Date-quality correction

Literacy Minnesota previously contained three month-only educator-resource records that had been normalized to the first day of their respective months. This normalization was removed because the exact publication day was not exposed. The exact-dated website corpus now retains only the March 6, 2026 Literacy Minnesota item. The three month-only records are preserved separately in:

`research_workspace/05_data/raw/communication_candidates_batch_52_LiteracyMN_month_only_unresolved.csv`

This correction preserves the no-invented-dates rule for weekly temporal analysis.

Volunteer Lawyers Network likewise has month-only study-window records preserved separately in:

`research_workspace/05_data/raw/communication_candidates_batch_49_VLN_month_only_unresolved.csv`

Keystone Community Services has two study-window newsletters whose exact publication dates are unresolved and preserved separately in:

`research_workspace/05_data/raw/communication_candidates_batch_40_Keystone_web_window_undated.csv`

These unresolved-date records remain available for qualitative or month-level analysis but are not assigned artificial dates for weekly time-series analysis.

## Companion completeness files

The one-to-one completeness-status companion-file cleanup is complete for the core TC001–TC084 sampling frame. The 27 organizations previously identified as having raw website data but no companion completeness record now have corresponding completeness-status files.

The companion records preserve exact-dated item counts while marking archives `partial_archive` wherever the full study-window website archive could not be demonstrated exhaustive. This means a zero-item organization must not be interpreted as communicatively silent unless its archive is demonstrably complete.

## Website-phase decision rule

The core website census is substantively and administratively complete for TC001–TC084 as of 2026-09-22, subject to ordinary downstream QC, deduplication, and normalization.

No organization with zero retrieved dated items should be interpreted as silent unless its archive is demonstrably complete. Partial-archive and retrieval-limitation statuses must remain visible in analysis.

## Website baseline locked for next phase

The website phase is now treated as the baseline corpus for cross-platform comparison. Do not reopen organizations merely because their archive is partial unless new first-party archive evidence is discovered during later reconciliation.

Before emotion or enforcement-relevance coding:

1. preserve exact-dated and unresolved-date records separately;
2. reconcile accidental duplicates while preserving deliberate cross-platform duplication;
3. normalize organization IDs, platform labels, dates, URLs, and content types;
4. preserve archive-completeness metadata alongside item-level data.

## Next phase

Proceed to the social-media census using the same full-census inclusion rule and the same study window, 2025-11-01 through 2026-03-31. Collect all publicly accessible organization communications from active sampled channels without filtering by immigration enforcement, emotion, political content, perceived importance, or relevance.

After social-media collection, reconcile website and social data, assign crosspost group identifiers where defensible, preserve platform-specific exposures, and normalize the combined corpus before emotion, appraisal, action-orientation, or enforcement-relevance coding begins.
