# Organization Inclusion and Exclusion Protocol

## Study purpose

This protocol defines the organizational universe for the Twin Cities immigration-enforcement communication study. The master registry is intentionally broader than the final analytical sample. Organizations may remain in the registry even when they are later excluded from content analysis, so that sampling decisions remain transparent and reproducible.

## Geographic scope

The study focuses on organizations based in or substantially operating in the Minneapolis–St. Paul Twin Cities metropolitan area.

An organization satisfies the geographic criterion if at least one of the following applies:

1. its headquarters are in the Twin Cities metro;
2. it maintains a staffed Twin Cities office or chapter;
3. it operates a substantial ongoing program in the Twin Cities metro; or
4. it is a statewide Minnesota organization whose immigrant/refugee work is substantially carried out in the Twin Cities.

Organizations with only incidental, one-time, or purely statewide/national activity in the metro do not satisfy this criterion.

## Population relevance

An organization satisfies the population criterion if immigrants, refugees, asylum seekers, newcomers, undocumented residents, or identifiable immigrant-origin communities are an explicit or substantial public of the organization.

Evidence may include:

- mission or about-page language;
- program descriptions;
- state or nonprofit service directories;
- immigrant-rights coalition membership;
- documented refugee-resettlement or immigration-legal work;
- culturally specific service to immigrant-origin communities; or
- sustained public communication directed to immigrant/refugee communities.

## Organizational eligibility

Eligible organizational forms include:

- nonprofit organizations;
- community-based organizations;
- immigrant- or refugee-led organizations;
- nonprofit legal-service organizations;
- advocacy and organizing organizations;
- refugee-resettlement organizations;
- faith-based nonprofits, ministries, coalitions, or programs with organized immigrant/refugee work;
- ethnocultural community organizations; and
- nonprofit economic/community-development organizations when immigrant/refugee communities are a substantial public.

## Master-registry inclusion criteria

An organization should enter the master registry when there is credible evidence that it satisfies all of the following:

1. **Twin Cities connection** — based in or substantially operating in the Twin Cities metro.
2. **Immigrant/refugee relevance** — immigrants, refugees, asylum seekers, newcomers, undocumented residents, or an immigrant-origin community are an explicit or substantial public.
3. **Civil-society character** — nonprofit, community-based, faith-based, legal-aid, advocacy, resettlement, or comparable noncommercial organization.
4. **Existence during the study period** — the organization existed and was not permanently closed before the study period.

Public communication about immigration enforcement is **not required** for entry into the master registry.

## Analytical-sample eligibility criteria

To enter the communication-analysis sample, a registry organization must additionally satisfy all of the following:

5. **Active during the study period** — operational at some point between October 1, 2025 and March 26, 2026.
6. **Public communication channel** — maintained at least one publicly accessible organizational communication channel during the study period, such as a website, Facebook, Instagram, X, YouTube, TikTok, LinkedIn, newsletter archive, or other public channel.
7. **Study-topic relevance** — published at least one item during the study period concerning immigration enforcement, ICE, detention/deportation, immigrant rights, federal immigration action, legal preparedness, community safety, know-your-rights information, raids/surge activity, or directly related consequences for immigrant/refugee communities.

## Exclusion criteria

An organization should be marked excluded from the analytical sample when one or more of the following applies:

- no meaningful Twin Cities operation;
- immigrant/refugee connection is incidental rather than substantial;
- government agency, elected office, school district, university unit, or other public institution rather than civil-society organization;
- commercial immigration law firm, consultancy, business, or other for-profit entity;
- individual activist account without a distinct organizational identity;
- organization permanently inactive before the study period;
- no identifiable public organizational communication during the study period;
- no study-relevant communication during the study period;
- duplicate program or chapter already captured under the parent organization;
- congregation with no organized immigrant/refugee-serving or immigration-advocacy program;
- national organization with no substantial Twin Cities organizational presence; or
- insufficient evidence to verify identity, activity, or organizational status.

## Registry status values

Use one of the following organization-level status values:

- `eligible`
- `probably_eligible`
- `excluded`
- `inactive`
- `duplicate`
- `unknown`

Every excluded, inactive, duplicate, or unknown organization must retain a short written reason in `exclusion_reason` or `status_notes`.

## Organizational typology

### Primary organizational role

Assign one primary role based on the organization's dominant immigrant/refugee-facing function during the study period:

- `ADV` — advocacy / organizing
- `LEG` — immigration legal / rights representation
- `RES` — refugee resettlement
- `SER` — direct social services
- `CBO` — ethnocultural / community-based organization
- `FAI` — faith-based immigrant/refugee support
- `DEV` — economic or community development
- `HYB` — genuinely hybrid organization for which no single role is dominant

A secondary role may also be recorded.

### Advocacy–service orientation

Record a separate five-point orientation variable:

1. primarily advocacy
2. advocacy-leaning hybrid
3. balanced hybrid
4. service-leaning hybrid
5. primarily service

This variable is analytically distinct from primary organizational role and should not be inferred solely from legal form or self-description.

### Faith affiliation

Record one of:

- `none/secular`
- `Christian`
- `Muslim`
- `Jewish`
- `interfaith`
- `other faith tradition`
- `faith-rooted but operationally secular`
- `unknown`

Faith affiliation should describe the organization, not the perceived religion of the community served.

## Evidence and verification rules

Where possible, verify each organization using at least two sources, prioritizing:

1. official organization website;
2. Minnesota government or recognized legal/service directory;
3. coalition/network membership directory;
4. established nonprofit research/reporting source;
5. official social-media account;
6. reputable local-news coverage.

Record source URLs and the date verified. Conflicting evidence should be documented rather than silently resolved.

## Unit of organization

The default unit is the legally or publicly identifiable organization. Programs should be coded separately only when they have a distinct public identity, communication channel, and operational role relevant to the study. Otherwise, program communication is attributed to the parent organization.

## Study period

October 1, 2025 through March 26, 2026, inclusive.

## Decision rule

When uncertain, retain the organization in the master registry with `probably_eligible` or `unknown` status rather than deleting it. Final exclusion should occur only after documenting the evidence and reason.