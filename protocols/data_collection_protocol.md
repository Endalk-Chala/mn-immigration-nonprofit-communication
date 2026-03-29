# Data Collection Protocol

**Study:** Strategic Communication and Immigration Enforcement  
**Study period:** October 1, 2025 – March 26, 2026  
**Version:** 1.0 Pre-Pilot

---

## Organizations and Typology

| Organization | Type Code | URL |
|---|---|---|
| Immigrant Law Center of MN (ILCM) | LS | ilcm.org/news/ |
| The Advocates for Human Rights | LS | theadvocatesforhumanrights.org |
| International Institute of MN (IIMN) | DS | iimn.org/news/ |
| Karen Organization of MN (KOM) | DS | mnkaren.org/resources/ |
| Arrive Ministries | DS | arriveministries.org/news-stories/ |
| MN Interfaith Coalition on Immigration (ICOM) | AO | mnicom.org/news/ |
| Unidos MN | AO | unidos-mn.org/media |

**Type codes:** LS = Legal-Service · DS = Direct-Service · AO = Advocacy-Oriented

---

## Relevance Screening — Two Gates

### Gate 1: Keyword Presence
Unit must contain at least one of:
- immigration / immigrant / immigrants
- ICE / Immigration and Customs Enforcement
- Operation Metro Surge / Operation PARRIS
- raid / raids
- deportation / deport
- detention / detain / detainee
- asylum / asylum seeker
- undocumented
- rapid response
- enforcement / immigration enforcement
- know your rights / KYR
- sanctuary
- family separation

### Gate 2: Substantive Relevance
Unit must do at least one of:
- Define, describe, or interpret immigration enforcement or its consequences
- Provide legal, practical, or protective information about enforcement
- Express organizational position on enforcement or immigrant rights
- Mobilize or direct action in response to enforcement
- Express solidarity with affected immigrant communities during enforcement period
- Report on organizational activities related to enforcement response

**Exclude:** Units where enforcement appears only as incidental framing for fundraising, program promotion, or staff recognition with no substantive enforcement engagement.

---

## Temporal Scope

**Start:** October 1, 2025  
**End:** March 26, 2026

- Website pages: include if published or meaningfully updated within window
- Facebook posts: up to 30 most recent enforcement-relevant posts per org per platform, reverse chronological order
- If no date visible: estimate from context clues and flag for verification

---

## Unit Recording Format

| Field | Format | Notes |
|---|---|---|
| Unit_ID | ORG-PLATFORM-NUM | e.g. ILCM-W-001, IIMN-FB-006 |
| Organization | Text | Full name |
| Org_Type | LS / DS / AO | |
| Platform | W / FB / X | Website / Facebook / X |
| URL | Text | Full URL or post identifier |
| Title_or_FirstLine | Text | Page title or first 100 chars |
| Date_Published | YYYY-MM-DD or estimate | Flag estimates with ~ |
| Keywords_Triggered | List | Which Gate 1 keywords present |
| Screener_Include | Y / FLAG / PENDING / N | |
| Full_Text_Retrieved | ★ FULL / Partial / PENDING | |
| Prelim_Codes | F/T/P/CTA/R shorthand | Pre-pilot estimates only |
| Notes | Text | Rationale, flags, analytical notes |

---

## Platform Collection Notes

**Website:** Direct URL fetch where possible; search indexing as fallback; manual browser for 403-blocked sites (ICOM).

**Facebook:** All Facebook pages block automated fetching via robots.txt. Manual browser collection required for all organizations. Log in to Facebook, visit each org page, scroll to October 2025, record all enforcement-relevant posts forward to March 26, 2026.

**Confirmed Facebook handles:**
- ILCM: facebook.com/immigrantlawcenterMN
- IIMN: facebook.com/IIMN.COMO ✓
- KOM: facebook.com/mnkarenorg ✓
- Arrive Ministries: facebook.com/arriveministries ✓
- The Advocates: verify via theadvocatesforhumanrights.org footer
- ICOM: verify via mnicom.org footer
- Unidos MN: verify via unidos-mn.org footer

---

## Exclusion Log

Units that fail Gate 1 or Gate 2 are logged with reason but not coded:
- General fundraising appeals with no enforcement-specific content
- Program success stories with no enforcement reference
- Staff/volunteer recognition posts
- Event announcements unrelated to enforcement
- Media roundup posts with no substantive content in the post itself
- Annual report posts without enforcement engagement
