# Eligibility Screening Summary v1

## Scope

The consolidated discovery frame contains **138 raw records** drawn from the original 84-record seed registry plus four discovery batches.

During screening, two non-independent records were identified:

1. **Navigate MN** is the former name of **Unidos MN** and should be merged with TC075.
2. **Monarca** appears to function as a program/initiative associated with **Unidos MN** rather than a separate organizational unit; preserve Monarca-branded communication as program-level material if verified, but do not count it as a separate organization.

This yields a current **deduplicated working universe of 136 distinct candidate organizational/program/network units** before resolving provisional cases.

## Screening outcomes across all 138 raw records

| Outcome | Raw records | Meaning |
|---|---:|---|
| Eligible | 91 | Meets current geography, population/mission, organizational-form, and study-period existence criteria |
| Probably eligible / verification needed | 23 | Plausible inclusion but requires one or more targeted checks |
| Excluded | 22 | Fails a defined criterion such as geography, organizational form, population relevance, or current program existence |
| Duplicate / alias / program merge | 2 | Do not count as independent organizational units |
| **Total** | **138** | Raw screening frame |

## Important methodological rule

**Public communication availability is not an organizational eligibility criterion.**

The screening process intentionally separates:

1. **Organizational universe eligibility** — Is the organization/program/network a relevant Twin Cities immigrant/refugee or identifiable immigrant-origin civil-society actor?
2. **Communication availability** — Did it maintain an official website and/or official social-media account during the study period (October 1, 2025–March 26, 2026), and is study-period content retrievable?
3. **Enforcement-related communication** — Did it publish relevant communication about immigration enforcement, ICE, raids, detention/deportation, rights, preparedness, public response, solidarity, assistance, or related enforcement impacts?
4. **Final analytical sample** — Organizations with retrievable, relevant communication items enter the framing/appraisal/emotion/action analysis.

This prevents the sampling frame from being defined by the dependent phenomenon of interest (whether an organization publicly communicated about enforcement).

## Next stage: communication-platform audit

For every eligible and probably eligible unit, create a platform registry with at least the following fields:

- `org_id`
- `organization_name`
- `unit_of_analysis`
- `official_website`
- `website_active_study_period`
- `website_archive_or_news_section`
- `facebook_url`
- `instagram_url`
- `x_url`
- `youtube_url`
- `tiktok_url`
- `other_platform_url`
- `official_account_verified`
- `platform_active_study_period`
- `study_period_content_retrievable`
- `earliest_retrievable_study_period_date`
- `latest_retrievable_study_period_date`
- `enforcement_related_content_found`
- `n_relevant_items_preliminary`
- `retrieval_method`
- `archive_or_capture_notes`
- `communication_completeness_rating`
- `final_analytical_sample_status`
- `exclusion_reason_analytical_sample`

## Communication-item unit

The emotion analysis should operate primarily at the **communication-item level** (post, webpage, statement, press release, video caption, newsletter item, etc.), not by labeling an organization itself as emotional.

Each included item can later be coded for:

- explicit and implicit emotional cues
- attributed emotion versus organizational voice
- appraisal dimensions (threat, injustice, responsibility, vulnerability, controllability, coping potential, etc.)
- emotion categories (fear, anxiety, anger, moral outrage, sadness/grief, compassion, empathy, hope, solidarity, care, reassurance, pride, defiance)
- emotional intensity (0–3)
- emotional function (mobilize, warn, reassure, regulate fear, build solidarity, generate empathy, moral evaluation, increase efficacy/control, comfort, resistance/defiance)
- action orientation (seek services, know rights, prepare, donate, volunteer, protest, contact officials, share information, support affected people, report enforcement activity, civic participation, etc.)

## Current methodological checkpoint

Do not begin full scraping yet. The next reproducible step is to resolve the 23 provisional organizational cases where feasible and, in parallel or immediately afterward, build the official website/social-media platform registry for eligible and provisional organizations.