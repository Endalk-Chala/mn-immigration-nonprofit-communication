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

## Companion completeness files still to add

The following 27 organizations already have website raw data but do not yet have a one-to-one companion completeness-status file. These are documentation gaps only, not substantive data-collection gaps:

- TC002 Cedar Riverside Adult Education Collaborative
- TC003 Centro Tyrone Guzman
- TC008 Literacy Minnesota
- TC015 Aeon
- TC016 Bridging
- TC019 Esperanza United
- TC021 IAFR Jonathan House
- TC025 Twin Cities Habitat for Humanity
- TC028 ACER
- TC030 African Development Center of Minnesota
- TC031 African Economic Development Solutions (AEDS)
- TC035 Arrive Ministries
- TC036 Catholic Charities Twin Cities
- TC037 CommonBond Communities
- TC038 CLUES
- TC042 Isuroon
- TC044 Minnesota Council of Churches
- TC047 Oromo Community of Minnesota
- TC049 PRISM
- TC050 Project for Pride in Living
- TC054 Alight
- TC055 CAPI USA
- TC056 Karen Organization of Minnesota
- TC064 The Advocates for Human Rights
- TC065 Volunteer Lawyers Network
- TC076 Minnesota Interfaith Coalition on Immigration (ICOM)
- TC077 ISAIAH

These should be repaired before final raw-to-interim consolidation, but they do not require reopening substantive website collection unless new archive evidence appears.

## Website-phase decision rule

The core website census is substantively complete for TC001–TC084 as of 2026-09-22. Remaining website work is quality-control and documentation cleanup, not discovery of unaudited core organizations.

No organization with zero retrieved dated items should be interpreted as silent unless its archive is demonstrably complete. Partial-archive and retrieval-limitation statuses must remain visible in analysis.

## Next phase

After companion-file cleanup, proceed to the social-media census using the same full-census inclusion rule. Website and social data should then be reconciled, cross-posts linked, exact-date versus month-only records separated, and the combined corpus normalized before emotion or enforcement-relevance coding begins.
