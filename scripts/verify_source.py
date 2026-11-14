"""Check the extraction snapshot without installing application dependencies."""
import hashlib
import json
from pathlib import Path
root = Path(__file__).resolve().parents[1]
record = json.loads((root / 'SOURCE_MANIFEST.json').read_text(encoding='utf-8'))
for item in record['files']:
    path = root / item['path']
    if not path.is_file() or path.is_symlink():
        raise SystemExit('Missing/nonregular extraction file: ' + item['path'])
    if hashlib.sha256(path.read_bytes()).hexdigest() != item['sha256']:
        raise SystemExit('Extraction file changed: ' + item['path'])
print('PASS: all recorded extraction files match SHA256')
