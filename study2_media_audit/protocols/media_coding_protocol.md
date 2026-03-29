# Study 2 — Media Coding Protocol
**Version:** 1.0  
**Study Period:** October 1, 2025 – March 26, 2026

---

## Unit of Analysis
Each article or media item in which at least one study organization is mentioned, quoted, or featured. One article = one codable unit, even if multiple organizations appear.

## Inclusion Criteria
- Published between October 1, 2025 and March 26, 2026
- Published in one of the nine target outlets
- Mentions, quotes, or features at least one of the seven study organizations
- Content relates to immigration, refugee services, or enforcement

## Exclusion Criteria
- Duplicate articles (same article indexed by multiple queries)
- Listicles or resource directories with no substantive content
- Articles where org name appears only in an advertisement or sidebar

---

## Variables

### 1. Appearance_Type
Code the primary way the organization appears in the article.

| Code | Label | Decision Rule |
|---|---|---|
| Q | Quoted as Source | Staff member directly quoted with name + org attribution |
| N | Named/Referenced | Org mentioned by name, no direct quote |
| O | Op-ed / Column | Piece authored by org staff |
| P | Press Release Pickup | ≥50% of article text matches org press release |
| E | Expert Commentary | Staff featured as SME without direct quote |
| S | Social Media Embedded | Org social post shown/screenshotted in article |
| A | Paid Advertisement | Labeled "Advertisement" or "Paid" |
| C | Sponsored Content | Labeled "Sponsored" or "Native" |

### 2. Paid_or_Unpaid
- **Unpaid:** Codes Q, N, O, P, E, S
- **Paid:** Codes A, C

### 3. Quote_Org_Verified
Did you personally verify the quote/mention by reading the article?
- Y = Yes, verified
- N = Not yet verified

### 4. Spokesperson_Named
Name of the staff member quoted or featured. Leave blank if org is named but no individual is quoted.

### 5. Frame_Match_Study1
Does the frame used in the media article match the primary frame this organization used in its own communication (Study 1 codebook)?
- Y = Frame matches
- N = Frame does not match
- P = Partial match
- U = Unable to determine

### 6. Dominant_Media_Frame
What frame does the article use to cover the organization?
Use Study 1 frame codes: F1 Legal Rights · F2 Human Rights · F3 Humanitarian Care · F4 Crisis/Emergency · F5 Justice/Advocacy · F6 Community Solidarity · F7 Policy Reform

---

## Inter-Rater Reliability Target
Krippendorff's α ≥ .80 for Appearance_Type and Dominant_Media_Frame before full coding.

---

## LexisNexis / ProQuest Search Protocol (Star Tribune + Pioneer Press)

**Search string:**
```
("Immigrant Law Center" OR "International Institute of Minnesota" OR 
"Advocates for Human Rights" OR "Arrive Ministries" OR 
"Karen Organization" OR "ICOM" OR "Unidos MN" OR "Monarca")
AND (immigration OR refugee OR ICE OR enforcement OR deportation)
```

**Date filter:** 10/01/2025 – 03/26/2026  
**Publication filter:** Star Tribune OR Saint Paul Pioneer Press  
**Content type:** News, Commentary, Editorial (exclude Classified, Legal Notices)

Add results manually to `media_coverage_raw.xlsx` following the same column structure.
