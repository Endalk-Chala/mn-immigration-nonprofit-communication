#!/usr/bin/env python3
"""Validate recovered network structure without third-party dependencies."""
import csv
import hashlib
import math
from collections import Counter
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data/network_snapshot_2026-09-26'

def main():
    nodes = list(csv.DictReader((DATA/'affective_circulation_r_layout_nodes_v1.csv').open()))
    edges = list(csv.DictReader((DATA/'affective_circulation_r_edges_v1.csv').open()))
    ids = {n['name'] for n in nodes}
    assert len(ids) == len(nodes) == 94
    assert Counter(n['node_type'] for n in nodes) == {'Affect':14, 'Organization':51, 'Media':29}
    assert len(edges) == 491
    assert len({(e['from'],e['to']) for e in edges}) == len(edges)
    for e in edges:
        assert e['from'] in ids and e['to'] in ids
        for field in ('raw_weight','weight','count'):
            assert math.isfinite(float(e[field])) and float(e[field]) > 0
    assert Counter(e['edge_type'] for e in edges) == {'Affect–organization':410, 'Organization–media':81}
    assert sum(float(e['raw_weight']) for e in edges if e['edge_type']=='Organization–media') == 120
    ns = {'g':'http://graphml.graphdrawing.org/xmlns'}
    graph = ET.parse(DATA/'affective_circulation_network_all_v1.graphml')
    normalize = lambda x: x.replace('A::','AFF::').replace('O::','ORG::').replace('M::','MED::')
    gids = {normalize(n.attrib['id']) for n in graph.findall('.//g:node',ns)}
    gedges = {(normalize(e.attrib['source']), normalize(e.attrib['target'])) for e in graph.findall('.//g:edge',ns)}
    assert len(gids) == 95 and gids-ids == {'ORG::TC049'} and not ids-gids
    assert {frozenset(p) for p in gedges} == {frozenset((e['from'],e['to'])) for e in edges}
    checksums = '\n'.join(f'{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.name}' for p in sorted(DATA.iterdir()) if p.suffix in {'.csv','.graphml','.png','.pdf','.svg'})+'\n'
    (DATA/'SHA256SUMS.txt').write_text(checksums)
    print('PASS: 491 matching edges; 120 story relations; documented isolated-node difference; checksums written.')

if __name__ == '__main__':
    main()
