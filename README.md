# Affective Intermediation in Twin Cities Nonprofit Communication

## Organizational emotion, public uptake, circulation, and action during immigration enforcement

**Status:** Active research project · data collection substantially complete · reliability pilot and full coding next  
**Author:** Endalkachew H. Chala  
**Study period:** November 1, 2025–March 31, 2026  
**Primary analytical universe:** 114 eligible/probably eligible organizational, program, and network units

## Project overview

This repository contains the data, sampling frame, protocols, platform audit, coding framework, and reproducible analysis workflow for a large-scale study of nonprofit and community communication during intensified immigration enforcement in the Twin Cities.

The project develops **affective intermediation** as a framework for examining how organizations interpret crisis, communicate emotion and appraisal, connect publics to resources and action, and how those messages are subsequently taken up, recirculated, contested, or converted into material or civic action.

The core analytical sequence is:

`crisis → organizational appraisal → affective production → public uptake → affective circulation → possible conversion/action`

The project therefore analyzes four linked empirical layers:

1. **Affective production** — what organizations communicate.
2. **Affective uptake** — how publics respond through visible comments and replies.
3. **Affective circulation** — how messages travel through shares, reposts, tagging, and cross-platform movement.
4. **Affective conversion** — observable movement toward helping, donating, volunteering, attending, protesting, seeking services, sharing resources, or other forms of coordination/action.

## Sampling frame

The consolidated discovery frame contains **138 raw records**.

Screening produced:

- **91 eligible** units
- **23 probably eligible / verification-needed** units
- **22 excluded** records
- **2 duplicate / alias / program-merge** records

The operational communication-census universe is therefore **114 independent eligible/probably eligible units**.

Important merge rules include:

- Navigate MN is treated as the former name/alias of Unidos MN, not as a separate organization.
- Monarca is treated as a Unidos MN program/initiative rather than an independent organizational unit.

Communication availability was never used as an eligibility criterion. An organization may belong in the sampling universe even when historical platform content is incompletely retrievable.

## Data architecture

The project includes:

- organization-level eligibility and sampling-frame data;
- website communication items;
- social-media communication items;
- social-platform account verification and archive-status data;
- cross-platform matched-message sets;
- post-level engagement snapshots;
- anonymized visible comment/reply interactions;
- recirculation evidence;
- external event chronology;
- coding templates and reliability pilot materials;
- reproducible dataset-building, validation, and analysis scripts.

### Important observability rule

Website communication is comparatively well observed. Historical Facebook, Instagram, X/Twitter, and some other platform archives are uneven and often incomplete. The social corpus is therefore treated as a **bounded public-web recovery with partial historical archives**, not as an exhaustive platform census.

A verified account with zero recovered historical posts is **not** interpreted as organizational silence.

Likewise, hidden engagement is `NA`, not zero.

## Affective intermediation coding

Each organization-owned communication item can be coded for:

- situational appraisal: threat, harm/loss, injustice, uncertainty, responsibility, vulnerability, coping efficacy, collective efficacy, care need, hope/opportunity;
- emotion intensity on a 0–3 scale: fear, anxiety/uncertainty, anger, moral outrage, grief/sadness, solidarity, care/compassion, empathy, hope, gratitude, pride, reassurance, defiance, urgency, and other emotions;
- communication function: inform, warn, reassure, regulate fear, mobilize, advocate, provide service, fundraise, build solidarity, generate empathy, moral evaluation, increase efficacy, mourn, document/testify, celebrate, encourage defiance;
- action orientation and specificity;
- audience, urgency, legal/service information, and resource provision;
- public uptake, circulation, and observable conversion-to-action signals.

**Engagement volume is not treated as emotion intensity.** Reactions, comments, shares, reposts, and views are relational/circulation measures; emotional meaning is coded separately from content and interaction.

## Current project status

Broad collection is frozen for analysis. The next substantive stage is:

1. build the analysis-ready corpus;
2. code the 40-item reliability pilot;
3. assess reliability and refine/freeze the codebook;
4. complete full-corpus coding;
5. merge and validate coding;
6. run descriptive, temporal, organizational-role, platform, matched-message, uptake, circulation, and conversion analyses;
7. develop the manuscript around the affective-intermediation model.

## Repository guide

The project grew iteratively, so the deepest working files remain in `research_workspace/` to preserve provenance and avoid breaking existing paths. The repository root now treats those files as the canonical flagship project rather than as a secondary workspace.

Key entry points:

- `research_workspace/01_sampling_frame/` — sampling frame and eligibility screening
- `research_workspace/02_protocols/` — collection and matched-message protocols
- `research_workspace/03_platform_registry/` — website/social account verification and archive status
- `research_workspace/05_data/` — raw, interim, processed, engagement, interaction, and matched-message data
- `research_workspace/06_codebooks/` — analytical schemas and affective-intermediation codebooks
- `research_workspace/07_analysis/` — build, validation, reliability, chronology, and analysis scripts
- `research_workspace/09_notes/` — research design, RQs, hypotheses, and conceptual notes

Top-level guide files are being used as stable entry points while the original paths remain intact for reproducibility.

## Analysis principles

The analysis separates:

- verified primary communication items;
- unresolved candidates;
- observed engagement cases;
- visible public-interaction cases;
- matched-message cases;
- excluded or duplicate organizations retained only for auditability.

Primary analyses will distinguish item-weighted from organization-normalized estimates and include robustness checks for sampling status, date precision, matched-message confidence, archive observability, and high-volume organizations.

## Earlier project history

This repository began with a smaller seven-organization nonprofit communication and media-relations design presented at AEJMC 2026. That earlier work is retained as project history and as a methodological precursor, but it no longer defines the repository's primary research identity.

The current flagship project is the 114-unit **Affective Intermediation** study.

## Citation

Until a final article or dataset release is published, cite the repository as an ongoing research project:

> Chala, Endalkachew H. (2026). *Affective Intermediation in Twin Cities Nonprofit Communication: Organizational Emotion, Public Uptake, Circulation, and Action During Immigration Enforcement*. GitHub research repository.

## Author

**Endalkachew H. Chala**  
[ORCID](https://orcid.org/0000-0001-6210-6706) · [Academic website](https://endalk-chala.github.io/) · [GitHub](https://github.com/Endalk-Chala)
