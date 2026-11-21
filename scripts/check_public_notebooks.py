#!/usr/bin/env python3
"""Check publication-copy notebooks for leftover outputs or unsafe command."""
import json
import re
from pathlib import Path

root=Path(__file__).resolve().parents[1]
paths=sorted((root/'notebooks').rglob('*.ipynb'))
assert len(paths)==14, f'Expected 14 notebooks; found {len(paths)}'
for path in paths:
    nb=json.loads(path.read_text(encoding='utf-8'))
    for i,c in enumerate(nb['cells']):
        if c['cell_type']!='code':continue
        assert not c.get('outputs'), (path,i,'outputs')
        assert c.get('execution_count') is None, (path,i,'execution count')
        s=''.join(c.get('source',[]))
        assert not re.search(r'!\s*rm\s+-rf\s+/content/drive(?:\s|$)',s), (path,i,'dangerous deletion')
print(f'PASS: {len(paths)} output-free notebook copies; destructive command disabled')
