# Platform Registry Schema

## Purpose

This registry bridges the organizational sampling frame to the communication dataset. Organizational eligibility and communication availability are deliberately separated.

An organization may be eligible for the sampling universe even if it ultimately has no retrievable public communication during the study period. Only organizations with retrievable, relevant communication enter the final item-level analytical sample.

## Study period

October 1, 2025–March 26, 2026.

## Organization-level communication audit fields

- `org_id`
- `organization_name`
- `eligibility_status`
- `unit_of_analysis_note`
- `official_website_url`
- `website_active_study_period`
- `website_archivable`
- `facebook_url`
- `facebook_official`
- `facebook_active_study_period`
- `facebook_retrievability`
- `instagram_url`
- `instagram_official`
- `instagram_active_study_period`
- `instagram_retrievability`
- `x_url`
- `x_official`
- `x_active_study_period`
- `x_retrievability`
- `youtube_url`
- `youtube_official`
- `youtube_active_study_period`
- `youtube_retrievability`
- `tiktok_url`
- `tiktok_official`
- `tiktok_active_study_period`
- `tiktok_retrievability`
- `linkedin_url`
- `linkedin_official`
- `linkedin_active_study_period`
- `linkedin_retrievability`
- `other_channel`
- `other_channel_url`
- `study_period_public_communication_found`
- `immigration_enforcement_related_content_found`
- `estimated_relevant_item_count`
- `retrieval_completeness`
- `archive_strategy`
- `communication_sample_status`
- `audit_date`
- `audit_notes`

## Controlled values

### Platform activity
- `yes`
- `no`
- `uncertain`
- `not_applicable`

### Retrievability
- `full`
- `partial`
- `limited`
- `none`
- `unknown`

### Retrieval completeness
- `complete_or_near_complete`
- `substantial_but_incomplete`
- `fragmentary`
- `none`
- `unknown`

### Communication sample status
- `include_for_item_collection`
- `provisional_include`
- `exclude_no_public_communication`
- `exclude_no_relevant_content`
- `exclude_not_retrievable`
- `pending_audit`

## Decision rules

1. **Do not use website/social-media availability to define organizational eligibility.** Organizational eligibility is determined first from geography, organizational form, mission/population relevance, and study-period existence.
2. **Use communication availability to determine analytical-sample eligibility.** An organization enters item-level collection only when official public communication is retrievable for the study period.
3. **Relevant communication must concern immigration enforcement or closely related response themes**, including ICE, raids, arrests/detention, deportation/removal, rights, legal preparedness, family preparedness, sanctuary, rapid response, community safety, mutual aid, enforcement-related fear/anxiety, protest, solidarity, or institutional response.
4. **Do not infer emotion from organization identity.** Emotion is coded at the communication-item level from textual, visual, audiovisual, or attributed emotional cues.
5. **Record platform absence separately from retrieval failure.** A platform may not exist, may exist but be inactive, or may be active but technically difficult to retrieve.
6. **Program-level organizations must be audited at the same level at which they qualified for inclusion.** For example, audit a refugee-services program rather than all communications from a broad parent organization when the broader parent is outside the substantive scope.
7. Preserve URLs, retrieval dates, archive locations, and completeness notes for reproducibility.

## Item-level bridge

Once an organization qualifies for collection, each retrieved communication item should receive a unique `item_id` and retain at minimum:

- organization / program
- platform
- publication date
- canonical URL
- archived copy/path
- content type
- text/caption/transcript
- language
- translation status
- enforcement relevance
- frame codes
- appraisal codes
- emotion codes
- emotional intensity
- emotional function
- action orientation
- coder and coding date
