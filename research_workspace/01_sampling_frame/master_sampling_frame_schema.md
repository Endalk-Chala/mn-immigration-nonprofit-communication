# Master Organization Sampling-Frame Schema

This document defines the organization-level registry used to construct and audit the Twin Cities immigrant/refugee nonprofit universe.

The master sampling frame is not the final analytical sample. It retains eligible, uncertain, excluded, inactive, and duplicate organizations so that sampling decisions are reproducible.

## Identification fields

| Field | Type | Description |
|---|---|---|
| `org_id` | string | Permanent study identifier, e.g. `TC001` |
| `organization_name` | string | Current official organization name |
| `alternate_name` | string | Acronym, former name, or common alternative name |
| `parent_organization` | string | Parent entity if organization is a program/chapter |
| `legal_entity_name` | string | Legal nonprofit name if different from public-facing name |

## Sampling and eligibility fields

| Field | Type | Description |
|---|---|---|
| `registry_status` | categorical | `eligible`, `probably_eligible`, `excluded`, `inactive`, `duplicate`, `unknown` |
| `analytical_sample_status` | categorical | `included`, `excluded`, `pending`, `not_assessed` |
| `exclusion_reason` | string | Required when excluded/inactive/duplicate |
| `status_notes` | string | Short rationale for uncertain or complex cases |
| `study_period_active` | boolean/unknown | Operational during Oct. 1, 2025–Mar. 26, 2026 |
| `public_channel_present` | boolean/unknown | At least one public communication channel during study period |
| `study_relevant_content_found` | boolean/unknown | At least one study-relevant communication item found |

## Geographic fields

| Field | Type | Description |
|---|---|---|
| `headquarters_city` | string | Headquarters city |
| `headquarters_state` | string | State |
| `primary_twin_cities_city` | string | Main Twin Cities location |
| `county` | string | Hennepin, Ramsey, Anoka, Dakota, Washington, etc. |
| `twin_cities_presence_type` | categorical | `headquarters`, `office`, `chapter`, `program`, `statewide_with_major_metro_operation`, `other` |
| `twin_cities_address_public` | string | Publicly listed organizational address when useful |
| `geographic_scope` | categorical | `neighborhood`, `city`, `metro`, `statewide`, `regional`, `national_with_local_branch` |

## Organizational-role fields

| Field | Type | Description |
|---|---|---|
| `primary_role` | categorical | `ADV`, `LEG`, `RES`, `SER`, `CBO`, `FAI`, `DEV`, `HYB` |
| `secondary_role` | categorical/string | Optional second role |
| `advocacy_service_orientation` | integer 1–5 | 1=primarily advocacy; 5=primarily service |
| `immigration_explicit_in_mission` | boolean/unknown | Immigration/newcomer focus explicitly stated |
| `refugee_resettlement` | boolean/unknown | Provides formal resettlement or newcomer services |
| `immigration_legal_services` | boolean/unknown | Immigration legal services/representation |
| `immigration_advocacy` | boolean/unknown | Policy advocacy, organizing, rights campaigns |
| `direct_services` | boolean/unknown | Direct material/social services |
| `economic_development` | boolean/unknown | Business, housing, workforce, financial development |
| `community_organizing` | boolean/unknown | Grassroots/member organizing |

## Faith and community fields

| Field | Type | Description |
|---|---|---|
| `faith_status` | categorical | `none/secular`, `Christian`, `Muslim`, `Jewish`, `interfaith`, `other faith tradition`, `faith-rooted but operationally secular`, `unknown` |
| `faith_notes` | string | Denomination/network or nuance if relevant |
| `community_specific` | boolean/unknown | Serves a named ethnocultural/national/language community |
| `communities_served` | string | Semicolon-separated community descriptors |
| `languages_publicly_used` | string | Languages observed on official channels |
| `immigrant_refugee_population_description` | string | Short description of the publics served |

## Official web presence

| Field | Type | Description |
|---|---|---|
| `website_url` | URL | Official website |
| `website_verified` | boolean | Verified as official |
| `website_active_study_period` | boolean/unknown | Website active during study period |
| `staff_page_url` | URL | Public staff/leadership page |
| `leadership_page_url` | URL | Leadership/board page if separate |
| `news_page_url` | URL | News/blog/press page |
| `resource_page_url` | URL | Immigration-rights/resource page when relevant |
| `newsletter_archive_url` | URL | Public newsletter archive |

## Social-platform presence

Store URLs here only after confirming they are official organizational accounts.

| Field | Type | Description |
|---|---|---|
| `facebook_url` | URL | Official Facebook page |
| `instagram_url` | URL | Official Instagram account |
| `x_url` | URL | Official X/Twitter account |
| `youtube_url` | URL | Official YouTube channel |
| `tiktok_url` | URL | Official TikTok account |
| `linkedin_url` | URL | Official LinkedIn page |
| `other_platform_name` | string | Telegram, Bluesky, WhatsApp channel, etc. |
| `other_platform_url` | URL | Official URL |

## Platform audit summary

| Field | Type | Description |
|---|---|---|
| `platform_audit_status` | categorical | `not_started`, `in_progress`, `complete`, `needs_recheck` |
| `active_platform_count` | integer | Number of active public channels during study period |
| `study_period_posting_confirmed` | boolean/unknown | At least one platform showed study-period activity |
| `first_relevant_item_date` | date | Earliest relevant communication located |
| `last_relevant_item_date` | date | Latest relevant communication located |
| `estimated_relevant_item_count` | integer/unknown | Preliminary count before collection |
| `scrape_feasibility` | categorical | `high`, `medium`, `low`, `manual_only`, `unknown` |
| `scrape_notes` | string | Technical/platform access notes |

## Source and provenance fields

| Field | Type | Description |
|---|---|---|
| `source_1_type` | string | official site, DHS, directory, coalition, etc. |
| `source_1_url` | URL | First evidence source |
| `source_2_type` | string | Independent second evidence source |
| `source_2_url` | URL | Second evidence source |
| `source_3_type` | string | Optional third source |
| `source_3_url` | URL | Optional third source |
| `verification_date` | date | Most recent registry verification |
| `verified_by` | string | Researcher/coder identifier |
| `source_conflict` | boolean | Conflicting organizational information found |
| `source_conflict_notes` | string | Explanation of conflict |

## Study-period enforcement communication fields

| Field | Type | Description |
|---|---|---|
| `ice_content_found` | boolean/unknown | Explicit ICE communication found |
| `detention_deportation_content_found` | boolean/unknown | Detention/deportation communication found |
| `know_your_rights_content_found` | boolean/unknown | Know-your-rights or preparedness content found |
| `metro_surge_content_found` | boolean/unknown | Explicit Metro Surge/surge response found |
| `federal_immigration_policy_content_found` | boolean/unknown | Federal immigration-policy communication found |
| `community_safety_content_found` | boolean/unknown | Safety/rapid-response communication found |
| `legal_resource_content_found` | boolean/unknown | Legal-help communication found |
| `advocacy_action_content_found` | boolean/unknown | Protest/contact officials/organizing content found |

## Data-management fields

| Field | Type | Description |
|---|---|---|
| `raw_data_folder` | string | Planned organization-specific raw-data path |
| `organization_slug` | string | Stable lowercase filesystem-safe organization name |
| `collection_status` | categorical | `not_started`, `partial`, `complete`, `blocked`, `manual_only` |
| `last_collection_date` | date | Latest collection attempt |
| `research_notes` | string | Free-text notes |

## Data rules

1. `org_id` must never be reused or reassigned.
2. Organization names may change, but historical names should be preserved in `alternate_name`.
3. Unknown values should be explicit (`unknown`) rather than silently treated as `no`.
4. URLs should be canonical organization/account URLs rather than search-result URLs.
5. Social accounts must be verified as official before entering them in the registry.
6. Excluded organizations remain in the master sampling frame.
7. The final analytical sample is derived from this registry; it is not maintained as a separate hand-curated list without provenance.
8. Every meaningful sampling decision should be supported by evidence and a verification date.