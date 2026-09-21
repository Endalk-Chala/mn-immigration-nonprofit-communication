# Completeness Report Schema

This project will report corpus completeness in two linked views: **organization-level** and **platform-level** coverage for the full-census study window, **2025-11-01 through 2026-03-31**.

## 1. Organization-level completeness
One row per eligible or probably eligible organization/program.

Fields:
- `org_id`
- `organization_name`
- `eligibility_status`
- `verified_official_channels_n`
- `channels_audited_n`
- `channels_complete_n`
- `channels_partial_n`
- `channels_unavailable_n`
- `total_items_collected`
- `website_items_n`
- `facebook_items_n`
- `instagram_items_n`
- `x_items_n`
- `youtube_items_n`
- `tiktok_items_n`
- `other_items_n`
- `earliest_item_date`
- `latest_item_date`
- `organization_collection_status`
- `organization_completeness_notes`

Recommended organization collection statuses:
- `complete_across_verified_channels`
- `complete_website_partial_social`
- `partial_multiple_channels`
- `social_only_partial`
- `no_retrievable_items`
- `pending_audit`

## 2. Platform-level completeness
One row per organization-platform pair.

Fields:
- `org_id`
- `organization_name`
- `platform`
- `official_channel_verified`
- `account_or_section`
- `account_url`
- `active_in_study_window`
- `archive_access_status`
- `items_collected_n`
- `earliest_visible_item_date`
- `latest_visible_item_date`
- `study_window_start_reached`
- `study_window_end_reached`
- `collection_status`
- `collection_method`
- `last_checked_date`
- `notes`

Allowed `archive_access_status` values:
- `complete_visible_archive`
- `partial_archive`
- `platform_blocks_history`
- `account_unavailable`
- `no_items_in_window`
- `channel_not_verified`

## 3. Cross-platform coverage matrix
A derived organization × platform table should show, for each organization, whether each channel is:
- `C` = complete
- `P` = partial
- `B` = blocked/inaccessible history
- `N` = no items in window
- `U` = unavailable/private/deleted
- `?` = channel not verified

Recommended columns:
`org_id, organization_name, website, facebook, instagram, x, youtube, tiktok, other, overall_status`

## 4. Interpretation rule
A missing communication item may be treated as noncommunication only when the relevant organization-platform archive is documented as `complete_visible_archive`. Otherwise, missingness is treated as an access limitation, not evidence of silence.

## 5. Analytical use
These reports will support:
1. denominator calculations for total organizational communication;
2. comparison of enforcement-related vs. non-enforcement communication;
3. assessment of organizational silence vs. data unavailability;
4. sensitivity analyses restricted to organizations/platforms with complete archives;
5. transparent reporting of platform-induced missingness in the methods and limitations sections.
