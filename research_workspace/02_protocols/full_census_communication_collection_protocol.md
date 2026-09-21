# Full-Census Communication Collection Protocol

## Study window
Collect all publicly accessible organizational communication published from **2025-11-01 through 2026-03-31**, inclusive.

## Organizational universe
Collect from every organization or program classified **eligible** or **probably eligible** in the organizational screening. Do not collect excluded organizations as analytical units. Do not double-count duplicate aliases or subordinate programs already merged into a parent unit unless the program itself is the defined unit of analysis.

## Channels
Audit every official public channel that can be verified for the organization during the study window:
- official website news/blog/press-release/event/resource pages
- Facebook
- Instagram
- X/Twitter
- YouTube
- TikTok
- other official public channels when clearly organizational and relevant

## Collection rule
Collect **every retrievable public communication item** in the study window, not only immigration-enforcement items. Enforcement relevance, framing, appraisal, emotion, and action orientation are coded only after corpus construction.

## One row per item
Each post, webpage, press release, statement, event notice, newsletter item, video, or other discrete communication is one row. Cross-posted identical items on different platforms remain separate platform observations but should carry a cross-post identifier where possible.

## Required fields
- `item_id`
- `org_id`
- `organization`
- `date`
- `platform`
- `account_or_section`
- `url`
- `content_type`
- `title_or_caption`
- `source_summary`
- `language`
- `media_type`
- `crosspost_group_id`
- `enforcement_relevance` (leave uncoded during raw collection when not yet assessed)
- `retrieval_date`
- `retrieval_status`
- `archive_or_capture_note`
- `collection_notes`

## Completeness rule
For each organization-platform pair, log one of:
- `complete_visible_archive` — all visible items in the window were captured
- `partial_archive` — only part of the historical archive is accessible
- `platform_blocks_history` — platform prevents reliable historical retrieval
- `account_unavailable` — official account unavailable/deleted/private
- `no_items_in_window` — verified active channel but no items in study window
- `channel_not_verified` — suspected channel could not be verified as official

A missing item must never be interpreted as noncommunication unless the archive is documented as complete.

## Copyright/data retention
Do not reproduce whole copyrighted posts in the public repository unless permitted. Preserve metadata, URLs, dates, short source-grounded summaries, and short excerpts only when analytically necessary. Raw captures that cannot be publicly redistributed should be stored outside the public repository or represented by an archive/capture note.

## Analytical sequencing
1. Finish organization-platform discovery.
2. Collect all items from Nov. 1, 2025 through Mar. 31, 2026.
3. Reconcile duplicates and cross-posts.
4. Produce completeness report by organization and platform.
5. Only then code enforcement relevance.
6. Then code frames, appraisals, emotions, emotional intensity, emotional function, and action orientation.
7. Then construct weekly temporal trajectories.
