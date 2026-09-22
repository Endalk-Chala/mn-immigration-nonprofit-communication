# Data architecture for website-social comparison

## Goal
Preserve source-specific raw data while making later analysis, visualization, and cross-platform comparison straightforward.

## Raw layer
Keep one raw file per organization-platform collection unit whenever practical, for example:
- `TC041_IIMN_website.csv`
- `TC041_IIMN_LinkedIn.csv`
- `TC041_IIMN_Facebook.csv`
- `TC041_IIMN_Instagram.csv`

Raw files should not be overwritten. Unresolved candidates remain in separate candidate files until date and canonical URL are verified.

## Interim normalized master
After collection, combine verified rows into one normalized table with one row per communication item. Required analytical fields should include:
- `item_id`
- `org_id`
- `organization`
- `date`
- `week`
- `platform`
- `platform_family` (`website` or `social_media`)
- `account_or_section`
- `url`
- `content_type`
- `title_or_caption`
- `source_summary`
- `language`
- `media_type`
- `crosspost_group_id`
- `retrieval_status`
- `archive_status`

Later coding fields should be added only after collection, including enforcement relevance, emotional cues, appraisal variables, emotional function, action orientation, and emotional intensity.

## Cross-post rule
The same message appearing on multiple platforms remains a separate observation on each platform. Use `crosspost_group_id` to link equivalent content across platforms. This allows analysis of whether wording, visuals, calls to action, or emotional intensity change by platform.

## Analysis advantages
This structure supports:
1. website vs social-media comparisons;
2. platform-specific emotional intensity trajectories;
3. organization-by-platform comparisons;
4. weekly time-series graphics;
5. emotion composition by platform;
6. paired cross-post comparisons;
7. sensitivity analyses that normalize for organizations with different posting volumes.

## Completeness rule
A missing row is not evidence of no communication unless that organization-platform archive is demonstrably complete for the full study window, 2025-11-01 through 2026-03-31.
