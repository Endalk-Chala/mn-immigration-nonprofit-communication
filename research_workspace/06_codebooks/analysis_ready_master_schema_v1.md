# Analysis-Ready Master Schema v1

## Purpose
This schema defines the final row structure for the analysis-ready communication dataset. One row = one organization-owned communication item on one native platform. Website and social-media versions remain separate observations even when matched to the same underlying message.

## Core identifiers
- `item_id` — unique communication-item identifier.
- `org_id` — final analytical organization/unit identifier.
- `organization` — standardized organization name.
- `analysis_inclusion_status` — `include`, `exclude_from_primary_analysis`, `program_level_only`, `duplicate_alias`.
- `sampling_status` — `eligible`, `probably_eligible`, `excluded`, `duplicate_merge`.
- `unit_of_analysis_note` — program-level or organizational restrictions.

## Time
- `date` — publication date where defensibly known.
- `date_precision` — `day`, `month`, `window_only`, `unknown`.
- `date_basis` — `publication_date`, `event_date`, `program_start_date`, `indexed_date`, `other`.
- `week_start` — Monday week start derived only for day-precision dates.
- `month` — YYYY-MM.
- `study_window` — boolean for 2025-11-01 through 2026-03-31.

## Platform and source
- `platform` — standardized: `website`, `linkedin`, `facebook`, `instagram`, `youtube`, `x`, `tiktok`, `threads`, `bluesky`, `other`.
- `platform_family` — `website` or `social`.
- `url` — canonical/native URL if available.
- `content_type` — normalized type such as `news`, `statement`, `event`, `resource`, `newsletter`, `post`, `video`, `fundraising`, `legal_guidance`, `service_update`, `other`.
- `title_or_caption` — source title/caption.
- `source_summary` — collection summary.
- `language` — observed primary language; multilingual allowed.
- `media_type` — `text`, `image`, `video`, `audio`, `mixed`, `unknown`.

## Retrieval and observability
- `retrieval_status` — `verified`, `partial`, `candidate`, `blocked`, `unresolved`, `unavailable`.
- `archive_status` — `complete_or_near_complete`, `partial_archive`, `not_enumerable`, `unknown`.
- `observability_weight_class` — descriptive only: `high`, `medium`, `low`; never used as a statistical weight unless separately justified.
- `capture_date` — date item was collected/verified.
- `collection_notes` — retrieval limitations and provenance.

## Matching and cross-platform correspondence
- `crosspost_group_id` — direct/near-direct crosspost group where available.
- `matched_message_id` — broader same-underlying-message identifier.
- `match_confidence` — `high`, `medium`, `low`, blank if unmatched.
- `adaptation_type` — `identical_crosspost`, `light_adaptation`, `platform_reframing`, `website_expansion`, `social_expansion`, `multimedia_adaptation`, blank.
- `publication_sequence` — within matched set, if known.

## Organizational role
- `org_role_primary` — `advocacy`, `legal`, `service`, `faith`, `ethnocultural`, `media_information`, `economic_development`, `housing`, `education`, `coalition_network`, `hybrid`, `other`.
- `org_role_secondary` — optional second role.
- `role_hybrid_flag` — boolean.

## Situational appraisal coding
- `threat_appraisal` — 0/1.
- `harm_loss_appraisal` — 0/1.
- `injustice_appraisal` — 0/1.
- `uncertainty_appraisal` — 0/1.
- `responsibility_blame_appraisal` — 0/1.
- `coping_efficacy_appraisal` — 0/1.
- `collective_efficacy_appraisal` — 0/1.
- `care_need_appraisal` — 0/1.
- `opportunity_hope_appraisal` — 0/1.
- `appraisal_notes` — brief rationale.

## Emotion coding
Multi-label emotion variables, each 0/1 unless unavailable:
- `emotion_fear`
- `emotion_anxiety_uncertainty`
- `emotion_anger`
- `emotion_grief_sadness`
- `emotion_solidarity`
- `emotion_care_compassion`
- `emotion_hope`
- `emotion_gratitude`
- `emotion_pride`
- `emotion_urgency`
- `emotion_reassurance`
- `emotion_other`

Additional emotion fields:
- `emotion_present` — 0/1.
- `emotion_explicitness` — `explicit`, `implicit`, `mixed`, `none`.
- `emotion_source` — `organization_voice`, `quoted_public`, `client_testimony`, `staff_testimony`, `community_collective`, `other`.
- `emotion_intensity` — ordinal 0–3: 0 none; 1 low; 2 moderate; 3 high.
- `emotion_notes` — rationale/quotation fragment kept short.

## Communication function
Multi-label 0/1 fields:
- `function_inform`
- `function_warn`
- `function_reassure`
- `function_mobilize`
- `function_advocate`
- `function_provide_service`
- `function_fundraise`
- `function_build_solidarity`
- `function_mourn_commemorate`
- `function_document_testify`
- `function_celebrate`
- `function_other`

## Action orientation
- `action_orientation_present` — 0/1.
- `action_type` — multi-value normalized list drawn from: `seek_legal_help`, `use_resource`, `attend_event`, `protest`, `contact_official`, `donate`, `volunteer`, `share_information`, `report_incident`, `prepare_documents`, `safety_plan`, `support_business`, `mutual_aid`, `other`.
- `action_specificity` — `none`, `general`, `specific`.
- `action_immediacy` — `none`, `low`, `moderate`, `high`.

## Audience and tone
- `audience_primary` — `immigrants_refugees`, `general_public`, `supporters_donors`, `policymakers`, `service_providers`, `workers`, `faith_community`, `ethnocultural_community`, `media`, `other`.
- `direct_address` — 0/1.
- `urgency_level` — 0–3.
- `legal_information_present` — 0/1.
- `service_information_present` — 0/1.
- `resource_link_present` — 0/1.

## Engagement snapshot
Joined by `item_id` where publicly observable:
- `engagement_capture_date`
- `like_or_reaction_count`
- `comment_count`
- `share_or_repost_count`
- `view_count`
- `organization_reply_count`
- `public_reply_count`
- `engagement_visibility_status`
- `engagement_retrieval_status`

Important: missing/hidden engagement is NA, not zero.

## Public uptake aggregates
Derived from interaction-level data:
- `visible_interaction_rows`
- `uptake_validation_count`
- `uptake_gratitude_count`
- `uptake_practical_inquiry_count`
- `uptake_help_request_count`
- `uptake_help_offer_count`
- `uptake_fear_count`
- `uptake_grief_count`
- `uptake_anger_count`
- `uptake_solidarity_count`
- `uptake_hope_count`
- `uptake_contestation_count`
- `uptake_resource_sharing_count`
- `uptake_coordination_count`
- `organization_response_visible` — 0/1/NA.

## Circulation
- `observed_recirculation_minimum` — minimum documented public repost/share traces when official count unavailable.
- `official_repost_share_count_available` — 0/1.
- `tagging_present` — 0/1/NA.
- `cross_org_tagging_present` — 0/1/NA.
- `circulation_notes`.

## Affective conversion
- `conversion_signal_present` — 0/1.
- `conversion_type` — normalized multi-value: `help_seeking`, `help_offering`, `donation`, `volunteering`, `event_attendance`, `protest_participation`, `service_connection`, `resource_referral`, `reporting_documentation`, `other`.
- `conversion_evidence_level` — `none`, `weak`, `moderate`, `strong`; based on observable interaction only, not inferred intention.

## Derived analytical fields
- `emotional_repertoire_count` — number of emotion categories coded present.
- `appraisal_count` — number of appraisal categories present.
- `function_count` — number of communication functions present.
- `engagement_total_observed` — sum only of metrics actually observed; do not impute hidden values.
- `enforcement_relevance` — coded later, not used for inclusion.
- `heightened_enforcement_period` — external chronology-based indicator applied after collection.

## Missing-data rules
- Blank/NA means not observed, not retrievable, or not applicable depending on companion status field.
- Numeric zero is used only when the platform explicitly shows zero or complete observation supports zero.
- Never convert hidden comments/shares into zero.
- Month-only records are excluded from weekly analyses but may remain in monthly/descriptive analyses.
- Candidate/unresolved items remain outside strict primary analyses until validated.
