# Data Collection Closure Memo — 2026-09-22

## Purpose

This memo freezes the current collection phase and defines what can and cannot be claimed about completeness before analysis begins.

## Study window

2025-11-01 through 2026-03-31 inclusive.

## Analytical universe

The final organizational universe is 114 independent eligible/probably eligible units after screening and deduplication. TC083 Navigate MN is merged with TC075 Unidos MN. D2-09 Monarca is treated as a program/initiative of Unidos MN rather than an independent organization.

Raw collection outside the final universe is preserved for auditability but must not be included automatically in the primary analysis. Examples include Aeon, Bridging, Twin Cities Habitat, VOA MN/WI, Catholic Charities Twin Cities, CommonBond, PRISM, PPL, and Fe y Justicia MN.

## Website collection status

The core TC001-TC084 website census is substantively and administratively complete under the project rules, subject to normal downstream QC, deduplication, normalization, and isolated omissions discovered through cross-platform reconciliation.

Website collection included all recoverable dated public communication in the study window rather than only immigration-, enforcement-, or emotion-related content. Routine service, legal, event, cultural, fundraising, educational, and organizational communication was retained as comparison material.

Some discovery-frame organizations also have verified website data, but the discovery extension is not uniformly exhaustive across all 114 organizations. Analysis should therefore distinguish the core website census from targeted discovery-frame website collection where relevant.

## Social-media collection status

The social-media corpus is a bounded public-web census with partial historical archives, not a complete platform census.

Official-account discovery was conducted systematically using the following hierarchy:
1. organization-owned website social links/icons;
2. official link hubs, newsletters, or organization-hosted directories;
3. canonical platform pages;
4. reliable public directories;
5. search-engine traces/reposts as fallback evidence.

The account-discovery audit checked 126 rows in total, including excluded and duplicate units, and reconciles to the 114-unit analytical universe after exclusions and deduplication.

Historical post recovery is uneven because LinkedIn, Facebook, Instagram, X/Twitter, TikTok, and YouTube expose different amounts of past content to the public web. LinkedIn yielded the strongest recoverable historical evidence. Facebook and Instagram were especially inconsistent through public indexing.

Therefore:
- a search miss must never be interpreted as organizational silence;
- zero verified posts does not mean zero posts existed;
- `partial_archive`, `unavailable`, and `url_unresolved` are retrieval states, not substantive communication states;
- platform-level prevalence statistics must use archive-availability controls/denominators rather than treating all 114 organizations as equally observable on every platform.

## Engagement and public-response status

Engagement data are an availability-based subcorpus nested within verified social posts, not a complete census of audience response.

Where publicly visible, the project captures:
- reactions/likes;
- comments;
- shares/reposts;
- views;
- visible reply chains;
- organization responses;
- anonymized comment content;
- assistance requests/offers;
- tagging and resource links;
- recirculation traces;
- evidence of movement toward coordination or action.

Engagement counts are capture-date snapshots. They should not be treated as contemporaneous counts at the time of original publication.

Unavailable engagement must be coded as unavailable/hidden, not zero.

High engagement is not a measure of emotional intensity. Engagement/circulation and emotional content must be modeled separately.

## Public-response privacy rule

Public commenter identities are not required for the primary research questions and should remain anonymized in the analytical dataset unless identity itself becomes substantively necessary and ethically justified.

## Cross-platform matching

Every native-platform item remains a separate observation. Cross-platform matching links corresponding items but never replaces them.

Matched-message analysis should use only high- or manually validated medium-confidence pairs/sets for strict within-message comparisons. Date proximity alone is insufficient.

## Unresolved candidates

Unresolved indexed candidates should remain outside strict verified-post counts unless a canonical or otherwise defensible first-party source is recovered. They may be used qualitatively as retrieval leads but should not be mixed with verified rows in quantitative analyses.

Examples include unresolved IIMN, Unidos MN, ILCM, and ACLU-MN LinkedIn candidates preserved in separate candidate files.

## Analysis-ready rules

Before analysis:
1. filter all communication items to the final 114-unit analytical universe;
2. enforce program-level unit restrictions for broad parent organizations;
3. preserve excluded-unit data separately as collection history/audit material;
4. create an archive-observability variable by organization × platform;
5. distinguish exact-dated, month-only, undated, and inferred/secondary date evidence;
6. keep engagement missingness distinct from observed zero;
7. link engagement/interactions/recirculation back to `item_id`;
8. retain matched-message identifiers for within-message platform analysis;
9. do not infer emotional intensity from reaction/share volume;
10. report the social corpus as partial historical public-web recovery rather than an exhaustive platform archive.

## Recommended analytical framing

The strongest defensible design is a multi-layer corpus:

**Layer 1: organizational communication** — website and verified social posts.

**Layer 2: platform adaptation** — matched messages across website/social channels.

**Layer 3: public uptake** — comments, replies, reactions, and organization responses where visible.

**Layer 4: circulation** — shares/reposts, tagging, and minimum observed recirculation traces.

**Layer 5: conversion/action** — observable requests, offers, referrals, participation, donation, volunteering, protest/event attendance, or practical coordination.

This supports the conceptual sequence:

crisis → organizational communication → public emotional/interpretive response → recirculation → collective interpretation → possible material or civic action

## Collection freeze

As of 2026-09-22, the corpus is frozen for transition into data cleaning and analysis. Additional material may be added later only as a clearly documented supplemental batch; earlier raw files should not be silently overwritten.
