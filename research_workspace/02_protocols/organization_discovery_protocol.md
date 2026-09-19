# Organization Discovery and Source-Triangulation Protocol

## Purpose

This protocol governs how organizations are discovered for the master Twin Cities immigrant/refugee nonprofit registry. The aim is coverage and reproducibility rather than reliance on a single directory.

## Core principle

No single source is treated as the definitive organizational universe. The master registry is built through source triangulation across government, nonprofit-research, legal-service, advocacy-network, faith/community, and organization-level sources.

## Discovery source classes

### A. Minnesota government sources

Use current Minnesota government directories to identify formal refugee, resettlement, legal, employment, health, and newcomer-service providers.

Priority source:
- Minnesota Department of Human Services — Resettlement Network Services provider list and map

Record the specific program relationship when available, e.g.:
- community workshops
- employment and career supports
- family resource connections
- immigration legal services
- refugee health promotion

### B. Twin Cities nonprofit landscape research

Use systematic nonprofit landscape studies to identify organizations that may not appear in immigration-specific state directories.

Priority source:
- Wilder Research, *Needs of Immigrants and the Nonprofit Landscape in the Twin Cities Region* (2024)

Important limitation: the Wilder scan focused on organizations serving Latin American and East African populations and providing housing and/or education. It therefore expands the sampling frame but does not define the complete universe.

### C. Immigrant-rights and rapid-response networks

Use immigrant-rights coalitions and networks to discover advocacy, faith, grassroots, labor, legal, and community organizations that may be absent from formal service directories.

Priority source:
- Immigrant Defense Network (IDN)

When membership is not publicly itemized, membership or participation should be verified through organization pages, coalition materials, event pages, public statements, or other independent evidence rather than assumed.

### D. Immigration legal-service directories

Use recognized legal-service directories to identify nonprofit immigration legal providers, DOJ-recognized programs, asylum representation organizations, and legal-aid groups.

Priority sources may include:
- Minnesota State Law Library / Minnesota Judicial Branch resource directories
- Minnesota DHS immigration legal-service listings
- DOJ-recognized organization directories where relevant

### E. Ethnocultural/community organization discovery

Search systematically for organizations serving specific Twin Cities immigrant-origin communities, including but not limited to:
- Somali
- Oromo
- Ethiopian/Eritrean
- Hmong
- Karen/Karenni
- Lao
- Cambodian
- Vietnamese
- Afghan
- Ukrainian
- Latino/Latine
- Liberian/West African
- broader African immigrant communities
- South Asian communities
- Middle Eastern/SWANA communities

Community-specific organizations should be retained in the master registry even when they are not immigration-policy organizations, provided immigrant/refugee populations are a substantial public.

### F. Faith-based organization discovery

Search Christian, Muslim, Jewish, interfaith, and other faith networks for organized immigrant/refugee programs.

Distinguish:
- congregation only;
- congregation with a structured immigrant/refugee program;
- separately incorporated faith-based nonprofit;
- interfaith coalition;
- faith-rooted organization operating as a largely secular service provider.

Ordinary congregations without organized immigrant/refugee work are not eligible.

### G. Snowball discovery

For every verified organization, review:
- partner pages;
- coalition memberships;
- referral/resource lists;
- funder/grantee lists;
- event co-sponsors;
- public statements signed jointly with other organizations;
- rapid-response resources;
- linked community partners.

New organizations discovered by snowballing enter the registry as `probably_eligible` or `unknown` until independently verified.

## Minimum discovery record

Every discovered candidate should initially receive:

- provisional organization name;
- source where discovered;
- source URL;
- discovery date;
- apparent Twin Cities connection;
- apparent immigrant/refugee relevance;
- provisional organizational role;
- provisional registry status.

## Verification sequence

For each candidate:

1. locate the official website or official public account;
2. verify Twin Cities presence;
3. verify immigrant/refugee population relevance;
4. verify organizational/civil-society status;
5. verify existence during the study period;
6. locate a second independent source;
7. assign registry status;
8. only later assess public-channel and study-topic eligibility for the analytical sample.

## Deduplication rules

Before creating a new `org_id`, check for:
- former organization names;
- acronyms;
- mergers;
- programs operating under a parent nonprofit;
- multiple offices of the same legal entity;
- rebranded organizations;
- local chapters of national organizations.

Do not create separate entries solely because an organization has several Twin Cities offices.

## Completeness strategy

Organization discovery continues until repeated searches across source classes produce no substantively new eligible organizations. The project should document the date of the latest discovery sweep rather than claim an eternally complete universe.

## Source audit log

Each discovery sweep should record:
- source searched;
- date searched;
- query or browsing method;
- number of candidate organizations found;
- number new to registry;
- number duplicates;
- number later excluded;
- notes on source limitations.

This allows the sampling frame to be updated over time while preserving how the original study universe was constructed.