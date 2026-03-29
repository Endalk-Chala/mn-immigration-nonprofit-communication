# Study 2 — Media Relations Audit
## Minnesota Immigration Nonprofit Coverage in Local Media

**Study period:** October 1, 2025 – March 26, 2026  
**Context:** Operation Metro Surge + Operation PARRIS  
**Companion to:** Study 1 — Nonprofit Digital Communication Content Analysis

---

## Research Questions

- **RQ1:** How frequently and in what roles do Minnesota immigration nonprofits appear in local media during the enforcement period?
- **RQ2:** Which organizational types (LS/DS) generate the most earned media coverage?
- **RQ3:** What types of media appearances predominate (quoted source, named reference, op-ed, press release pickup)?
- **RQ4:** Do the frames nonprofits use in their own digital communication transfer to media coverage of those organizations? *(Framing transfer hypothesis — bridge to Study 1)*

---

## Outlets Covered

| Outlet | Type | Access | Method |
|---|---|---|---|
| MPR News | Public radio / digital | Open | Automated scraper |
| Sahan Journal | Ethnic / community media | Open | Automated scraper |
| MinnPost | Digital nonprofit news | Open | Automated scraper |
| Axios Twin Cities | Digital newsletter | Open | Automated scraper |
| Bring Me The News | Digital aggregator | Open | Automated scraper |
| Star Tribune | Legacy newspaper | Paywalled | LexisNexis / ProQuest |
| Pioneer Press | Legacy newspaper | Paywalled | LexisNexis / ProQuest |
| WCCO | Broadcast TV | Partial | Online article archive |
| KARE 11 | Broadcast TV | Partial | Online article archive |

---

## Organizations Tracked

| Organization | Type | Abbreviation |
|---|---|---|
| Immigrant Law Center of MN | Legal-Service (LS) | ILCM |
| The Advocates for Human Rights | Legal-Service (LS) | ADV |
| International Institute of MN | Direct-Service (DS) | IIMN |
| Arrive Ministries | Direct-Service (DS) | ARR |
| Karen Organization of MN | Direct-Service (DS) | KOM |
| MN Interfaith Coalition on Immigration | Advocacy-Oriented (AO) | ICOM |
| Unidos MN / Monarca | Advocacy-Oriented (AO) | UMN |

---

## Appearance Type Coding

| Code | Label | Definition |
|---|---|---|
| Q | Quoted as Source | Org staff directly quoted with attribution |
| N | Named/Referenced | Org mentioned but not directly quoted |
| O | Op-ed / Column | Piece authored by org staff |
| P | Press Release Pickup | Article reproduces org press release substantially verbatim |
| E | Expert Commentary | Org staff featured as subject matter expert |
| S | Social Media Embedded | Org social media post embedded or screenshotted in article |
| A | Paid Advertisement | Clearly labeled paid placement |
| C | Sponsored Content | Labeled sponsored/native advertising |

---

## Paid vs. Unpaid Classification

**Unpaid (Earned Media):** Q, N, O, P, E, S  
**Paid:** A, C

Note: The overwhelming majority of nonprofit immigration coverage is expected to be earned media. Paid placements should be flagged and verified manually.

---

## File Structure

```
study2_media_audit/
├── scrapers/
│   └── media_scraper.py          ← Run this first
├── data/
│   ├── raw/
│   │   ├── media_coverage_raw.xlsx    ← Scraper output
│   │   └── media_coverage_raw.csv
│   └── processed/
│       └── media_coverage_coded.xlsx  ← After manual coding
├── analysis/
│   ├── tables/                        ← Frequency tables, cross-tabs
│   └── figures/                       ← Charts, visualizations
└── protocols/
    └── media_coding_protocol.md       ← Coding instructions
```

---

## How to Run

```bash
cd C:\Users\endal\OneDrive\Desktop\PR
python study2_media_audit\scrapers\media_scraper.py
```

---

## Theoretical Framework

- **Agenda building** (Berkowitz 1987; Turk 1986) — nonprofits as information subsidies for journalists
- **Source credibility** (Morton & Warren 1992) — which org types are preferred sources
- **Framing transfer** (Entman 1993; Hallahan 1999) — do nonprofit frames appear in coverage?
- **Earned vs. paid media** (Kitchen & Burgmann 2010) — nonprofit PR resource constraints
