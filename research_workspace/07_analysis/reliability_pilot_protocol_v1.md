# Reliability Pilot Protocol v1

## Goal
Test and refine the affective-intermediation coding scheme before full-corpus coding.

## Pilot sample
Target 40 items, stratified so the pilot is not dominated by high-volume organizations or one platform.

Recommended allocation:
- 20 website items
- 20 social-media items where available
- spread across Nov. 2025, Dec. 2025, Jan. 2026, Feb. 2026, Mar. 2026
- include advocacy/legal/service/ethnocultural/faith/hybrid roles
- include both visibly emotional and apparently procedural/routine items
- do not select only enforcement-related items

If social availability cannot support 20 distinct eligible items, use all verified eligible social items up to that number and fill the remainder with website items while preserving role/month variation.

## Coding procedure
1. Freeze codebook version before pilot coding.
2. Code each pilot item independently without viewing aggregate results.
3. If a second coder is available, both coders code the same 40 items.
4. If only one coder is available, perform a blinded recode after a meaningful interval and shuffle item order.
5. Record `coder_confidence` as high/medium/low; confidence is diagnostic, not part of substantive findings.

## Reliability statistics
- Binary appraisal/function variables: Cohen's kappa (two coders) or Krippendorff's alpha if needed.
- Nominal variables: Cohen's kappa / Krippendorff's alpha nominal.
- Ordinal 0–3 emotion intensity variables: weighted kappa and/or Krippendorff's alpha ordinal.
- Continuous derived composites are not reliability-coded directly; derive them only after item-level variables reach acceptable reliability.

## Interpretation
Do not use a single mechanical cutoff. Examine coefficient values, prevalence imbalance, disagreement pattern, and theoretical importance.

Suggested diagnostic ranges only:
- >= .80: strong agreement
- .67–.79: usable with review
- .50–.66: revise definitions/training and recode
- < .50: substantial revision required

These ranges are diagnostics rather than publication claims.

## Disagreement review
For every variable below the acceptable range:
1. inspect disagreement cases;
2. identify whether the problem is category overlap, unclear evidence threshold, intensity boundary, or source attribution;
3. add examples/boundary rules to codebook;
4. recode pilot;
5. recompute reliability.

## Especially important boundary checks
- anger vs moral outrage
- fear vs anxiety/uncertainty
- care/compassion vs empathy
- hope vs reassurance
- solidarity vs pride
- organizational emotion vs attributed public emotion
- procedural legal/service information vs reassurance/fear regulation
- mobilization vs general advocacy
- action orientation vs merely informational resource provision

## Freeze point
After acceptable pilot reliability, create `affective_intermediation_coding_codebook_v2_frozen.md` if revisions were made. Full-corpus coding should use the frozen version. Any later substantive coding-rule change must be documented and affected items recoded.
