# Strategic Communication and Immigration Enforcement
## A Quantitative Content Analysis of Twin Cities Nonprofit Multi-Platform Digital Communication

[![Status](https://img.shields.io/badge/Status-Data%20Collection%20in%20Progress-yellow)]()
[![Study 1](https://img.shields.io/badge/Study%201-Content%20Analysis-blue)]()
[![Study 2](https://img.shields.io/badge/Study%202-Media%20Relations%20Audit-green)]()
[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)]()
[![Target Journal](https://img.shields.io/badge/Target-JPRR-red)]()

---

**Author:** Endalkachew H Chala  
**Study Period:** October 1, 2025 – March 26, 2026  
**Enforcement Context:** Operation Metro Surge + Operation PARRIS (Twin Cities, MN)  
**Target Journal:** Journal of Public Relations Research (JPRR)

---

## Overview

This repository contains data, code, and documentation for a two-study research project examining how nonprofit organizations serving immigrant and refugee communities in the Twin Cities metropolitan area strategically communicated during a period of unprecedented federal immigration enforcement.

Between December 2025 and March 2026, the U.S. Department of Homeland Security deployed over 3,000 federal agents to the Twin Cities under **Operation Metro Surge**, with a parallel operation — **Operation PARRIS** — targeting lawfully resettled refugees. This project documents how seven nonprofit organizations across three organizational types responded communicatively across website and Facebook platforms, and how local media covered those organizations during the same period.

---

## Repository Structure

```
/
├── data/
│   ├── raw/
│   │   ├── full_data_log.xlsx        # Master data log — 116+ units, 7 organizations
│   │   └── text_corpus.txt           # Plain-text corpus for NVivo/Atlas.ti
│   ├── coded/                        # Post-pilot coded data (in progress)
│   └── codebook/
│       └── codebook_protocol.docx    # Full codebook + data collection protocol
│
├── analysis/
│   ├── tables/                       # Frequency tables, chi-square, Cramér's V
│   └── figures/                      # Visualizations
│
├── paper/
│   └── paper_draft_v7.docx           # Current manuscript draft
│
├── protocols/
│   └── data_collection_protocol.md   # Sampling and screening protocol
│
└── study2_media_audit/               # Study 2 — Media Relations Audit
    ├── scrapers/
    │   ├── scrape_ian_mn.py          # IAN MN nonprofit directory scraper
    │   ├── digital_audit.py          # Nonprofit digital presence auditor
    │   └── media_scraper.py          # 5-outlet local media scraper
    ├── data/raw/                     # Scraped media coverage data
    ├── data/processed/               # Coded media coverage data
    ├── analysis/
    └── protocols/
        └── media_coding_protocol.md  # Media appearance coding instructions
```

---

## Study 1 — Nonprofit Digital Communication Content Analysis

### Theoretical Framework

| Framework | Key Scholars |
|---|---|
| Nonprofit PR & relationship management | Hon & Grunig (1999); Ledingham & Bruning (2000) |
| Civil society enactment theory | Taylor (2009, 2010); Taylor & Doerfel (2003) |
| Framing theory | Entman (1993); Hallahan (1999) |

### Sample

**Sampling frame:** Immigration Advocates Network National Legal Services Directory (MN), DOJ/EOIR Recognition & Accreditation Roster, MN Department of Health Resettlement Agency Registry.

| Organization | Type | Website | Facebook | Total |
|---|---|---|---|---|
| Immigrant Law Center of MN (ILCM) | Legal-Service (LS) | 7 | 42 | **49** |
| The Advocates for Human Rights | Legal-Service (LS) | 6 | 15 | **21** |
| International Institute of MN (IIMN) | Direct-Service (DS) | 7 | 16 | **23** |
| Arrive Ministries | Direct-Service (DS) | 4 | 10 | **14** |
| Karen Organization of MN (KOM) | Direct-Service (DS) | 2 | — | 2 |
| MN Interfaith Coalition on Immigration (ICOM) | Advocacy-Oriented (AO) | 5 | — | 5 |
| Unidos MN | Advocacy-Oriented (AO) | 1 | — | 1 |
| **Total** | | **32** | **83** | **115** |

### Codebook — 5 Variables, 37 Codes

| Variable | Codes |
|---|---|
| **FRAME1 / FRAME2** | F1 Legal Rights · F2 Human Rights · F3 Humanitarian Care · F4 Crisis/Emergency · F5 Justice/Advocacy · F6 Community Solidarity · F7 Policy Reform |
| **TONE1 / TONE2** | T1 Urgent · T2 Reassuring · T3 Informational · T4 Mobilizing · T5 Compassionate · T6 Confrontational |
| **TPUB** | P1 Immigrants/Families · P2 Donors · P3 Volunteers · P4 Policymakers · P5 General Public · P6 Coalition Partners |
| **CTA** | CTA0 None · CTA1 Legal Help · CTA2 Donate · CTA3 Volunteer · CTA4 Attend Event · CTA5 Contact Lawmakers · CTA6 Share Resources · CTA7 Report Enforcement |
| **ROLE** | R1 Legal Advocate · R2 Service Provider · R3 Crisis Responder · R4 Community Defender · R5 Coalition Builder · R6 Public Educator |

### Research Questions & Hypotheses

| | Question |
|---|---|
| **RQ1** | Do organizational types differ in dominant communication frames? |
| **RQ2** | Do organizational types differ in dominant tone? |
| **RQ3** | Do organizational types differ in target publics? |
| **RQ4** | Do organizational types differ in calls to action? |
| **RQ5** | Do organizational types differ in projected organizational role? |
| **RQ6** | Do platforms (website vs. Facebook) differ in framing within the same sample? |
| **H1** | LS orgs will use legal rights (F1) and human rights (F2) frames more than DS orgs |
| **H2** | DS orgs will use humanitarian care (F3) and crisis (F4) frames more than LS orgs |
| **H3** | AO orgs will use justice/advocacy (F5) and policy reform (F7) frames more than LS/DS orgs |
| **H4** | LS orgs will target policymakers (P4) more; DS orgs will target immigrants/families (P1) more |
| **H5** | AO orgs will show greater cross-platform framing consistency than DS orgs |

### Two-Gate Relevance Screening Protocol

**Gate 1 — Keyword presence:**
ICE · immigration enforcement · Operation Metro Surge · Operation PARRIS · raid · deportation · detention · asylum · undocumented · rapid response · know your rights · sanctuary · family separation

**Gate 2 — Substantive relevance:** Unit must define/describe enforcement, provide protective information, express organizational position, mobilize action, express solidarity, or report enforcement-response activities.

### Reliability Target
Krippendorff's α ≥ .80 for all five variables before full coding begins.

---

## Study 2 — Media Relations Audit

A companion study mapping how nine local media outlets covered the same seven organizations during the same enforcement period. Examines earned vs. paid media, source roles, and whether nonprofit communication frames transfer to media coverage (framing transfer hypothesis).

### Outlets

| Outlet | Type | Access |
|---|---|---|
| MPR News | Public radio / digital | Automated scraper |
| Sahan Journal | Ethnic / community media | Automated scraper |
| MinnPost | Digital nonprofit news | Automated scraper |
| Axios Twin Cities | Digital newsletter | Automated scraper |
| Bring Me The News | Digital aggregator | Automated scraper |
| Star Tribune | Legacy newspaper | LexisNexis / ProQuest |
| Pioneer Press | Legacy newspaper | LexisNexis / ProQuest |
| WCCO | Broadcast TV | Manual (online archive) |
| KARE 11 | Broadcast TV | Manual (online archive) |

### Theoretical Bridge to Study 1
**Framing transfer hypothesis:** Do the F1–F7 frames organizations use in their own digital communication predict the frames that appear in media coverage of those organizations?

---

## Python Scripts

| Script | Purpose |
|---|---|
| `study2_media_audit/scrapers/scrape_ian_mn.py` | Builds sampling frame from IAN MN nonprofit directory |
| `study2_media_audit/scrapers/digital_audit.py` | Audits nonprofit websites for social media presence, staff, languages, counties |
| `study2_media_audit/scrapers/media_scraper.py` | Scrapes 5 open-access outlets for org mentions and appearance type |

**Install dependencies:**
```bash
pip install requests beautifulsoup4 openpyxl pandas
```

**Run scrapers:**
```bash
# Step 1 — Build sampling frame
python study2_media_audit/scrapers/scrape_ian_mn.py

# Step 2 — Audit digital presence
python study2_media_audit/scrapers/digital_audit.py

# Step 3 — Scrape media coverage
python study2_media_audit/scrapers/media_scraper.py
```

---

## Data Collection Status

| Phase | Task | Status |
|---|---|---|
| 1 | Codebook development | ✅ Complete |
| 2 | Sampling frame construction | ✅ Complete |
| 3 | Website data collection — all 7 orgs | ✅ Complete |
| 4 | Facebook — ILCM, IIMN, ADV, Arrive Ministries | ✅ Complete |
| 5 | Facebook — KOM, ICOM, Unidos MN | 🔄 In Progress |
| 6 | Pilot coding + inter-rater reliability | ⏳ Pending |
| 7 | Full coding | ⏳ Pending |
| 8 | Statistical analysis | ⏳ Pending |
| 9 | Study 2 — Media scraping | 🔄 In Progress |
| 10 | Study 2 — Media coding + analysis | ⏳ Pending |

---

## Key Preliminary Observations

- **ILCM** uses the most confrontational language in the corpus: "ethnic cleansing," "occupation," "murder," "authoritarian fascism"
- **The Advocates** uniquely invokes international legal standards: "extrajudicial killing," "Minnesota Protocol," "as required under international law"
- **IIMN** suspended all in-person services due to ICE activity (January 2026) — direct evidence of enforcement chilling effect on nonprofit service delivery
- **Arrive Ministries** is the only faith-based organization in the sample; the only org using "pray" as a mobilization CTA
- **Julia Decker (ILCM Policy Director)** is quoted in 11 of 42 ILCM Facebook posts — the most prominent organizational spokesperson in the corpus
- **Cross-platform finding:** The Advocates leads with human dignity quotes on Facebook and legal mechanics on the website for the same events

---

## Citation

> Chala, E. H. (in preparation). Strategic communication and immigration enforcement: A quantitative content analysis of Twin Cities nonprofit multi-platform digital communication. *Journal of Public Relations Research.*

---

*Endalkachew H Chala*
