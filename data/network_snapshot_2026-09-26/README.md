# Recovered circulation-network snapshot — September 26, 2026

Author: Endalkachew H. Chala. Study period: November 1, 2025–March 31, 2026.

These are unchanged recovered analytical exports, not a newly coded dataset. The source working manuscript reports 337 communication items from 44 organizations and a 114-unit operational sampling universe. Independent coding reliability has not been verified for this release.

## Files and fields

- `affective_circulation_r_edges_v1.csv`: 491 edges. `from` and `to` are node identifiers; `edge_type` distinguishes affect–organization and organization–media edges; `raw_weight`, `weight`, and `count` preserve the original export values. The manuscript describes affect–organization `weight` as organization-normalized affect intensity; organization–media weights represent unique story relations. Exact upstream aggregation should be verified against the original script before recalculation. These are not audience emotion or influence measures.
- `affective_circulation_r_layout_nodes_v1.csv`: 94 nodes. `name` is the identifier, `label` the display name, `node_type` the layer, `degree` and `strength` exported connectivity measures, `label_priority` a display setting, and `x`/`y` saved layout coordinates. Original centrality computation details are not included.
- `affective_circulation_network_all_v1.graphml`: 95 nodes and 491 edges. Prefixes A::, O:: and M:: correspond to AFF::, ORG:: and MED:: in the R CSVs. Organization TC049 is present in GraphML but absent from the R layout; no edge refers to it. This accounts for the node-count difference.
- The publication-view PDF preserves the recovered R rendering. Other layouts remain outside this snapshot. Visual suppression of weak ties does not delete them from the edge CSV.
- `SHA256SUMS.txt`: checksums of recovered files for byte-level integrity.

## Interpretation and reuse

The integrated graph links organizational affect repertoires with verified media visibility. It does not establish that a particular emotional frame traveled from a post to a news story, nor that audiences experienced the coded emotions. Matched-message evidence is needed for frame-transmission claims.

Historical social archives are partial; missing posts are not organizational silence, and unavailable engagement is not zero. The snapshot provides network reuse and structural validation, not full item-to-figure reproduction. The completed item-level coding, reliability results, original R script and story-level verification table are not included in this recovered snapshot.

The repository MIT license remains in place. Reuse does not confer rights to third-party source material. Cite the author, repository, and exact commit used; no dataset DOI is assigned by this snapshot.
