# Twin Cities Immigration Nonprofit Communication Project

Working research workspace for building the organizational sampling frame, platform registry, scraping infrastructure, coding protocols, and analysis for the Twin Cities immigration-enforcement communication study.

## Folder structure
- `01_sampling_frame` — master organization universe and eligibility decisions
- `02_protocols` — inclusion/exclusion and data-collection protocols
- `03_platform_registry` — websites and social-media account registry
- `04_scraping/scripts` — scraping and collection scripts
- `04_scraping/logs` — retrieval logs and errors
- `05_data/raw` — untouched collected data
- `05_data/interim` — cleaned but not final data
- `05_data/processed` — analysis-ready datasets
- `06_codebooks` — framing, emotion, appraisal, and action codebooks
- `07_analysis/tables` — analysis tables
- `07_analysis/figures` — figures and plots
- `08_paper` — manuscript drafts and notes
- `09_notes` — research decisions and working notes

## Data principles
1. Never overwrite raw data.
2. Keep original captures in `05_data/raw`.
3. Document all transformations from raw to interim to processed data.
4. Keep organization-level sampling decisions separate from post-level coding.
5. Preserve source URLs, retrieval dates, and platform metadata whenever possible.
6. Do not commit private, sensitive, copyrighted, or platform-restricted raw material unless redistribution is clearly permitted.

## Current status
This workspace is a development scaffold. Sampling-frame construction, inclusion/exclusion criteria, platform auditing, scraping methods, and the emotion/appraisal codebook are still being developed.
