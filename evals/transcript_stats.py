"""Measure a generated panel answer: turns, turn length, summary size, footnoted quotes."""
import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TURN = re.compile(r'^(?:↳\s*)?\*\*([^*]+)\*\*\s+(.+)$')


def section(text, title):
    match = re.search(rf'^## {re.escape(title)}[^\n]*\n(.*?)(?=^## |\Z)', text, re.M | re.S)
    return match.group(1) if match else ''


def transcript(text):
    return section(text, '회의록') or section(text, '댓글')


def sentences(line):
    line = re.sub(r'\([^)]*\)', '', line)
    line = re.sub(r'\[\d+\]', '', line)
    parts = re.split(r'(?<=[.!?…])\s+', line.strip())
    return len([p for p in parts if re.search(r'[가-힣A-Za-z0-9]', p)])


def turns(text):
    return [(m.group(1).strip(), m.group(2)) for m in map(TURN.match, transcript(text).splitlines()) if m]


def registered_quotes(root):
    found = set()
    for profile in (root / 'people').glob('*.md'):
        found.update(re.findall(r'^\s+- "([^"]+)"', profile.read_text(encoding='utf-8'), re.M))
    return found


def stats(text, root=ROOT):
    pairs = turns(text)
    speakers = {}
    for name, _ in pairs:
        speakers[name] = speakers.get(name, 0) + 1
    cited = re.findall(r'"([^"]+)"', section(text, '각주'))
    known = registered_quotes(root)
    return {
        'chars': len(text),
        'turns': len(pairs),
        'speakers': speakers,
        'long_turns': [{'speaker': n, 'sentences': sentences(t)} for n, t in pairs if sentences(t) > 4],
        'summary_lines': len([line for line in section(text, '정리').splitlines() if line.strip()]),
        'cited_quotes': cited,
        'unregistered_quotes': [q for q in cited if q not in known],
    }


def blind(text):
    """Replace panel speaker names with 화자 N and mask mentions; 진행자 stays visible."""
    pairs = turns(text)
    names = sorted({n for n, _ in pairs if n != '진행자'}, key=len, reverse=True)
    key, lines = [], []
    for line in transcript(text).splitlines():
        m = TURN.match(line)
        if m and m.group(1).strip() != '진행자':
            key.append(m.group(1).strip())
            line = f'**화자 {len(key)}** {m.group(2)}'
        for name in names:
            line = line.replace(name, '○○')
        lines.append(line)
    return '\n'.join(lines).strip(), key


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('file')
    parser.add_argument('--blind', action='store_true', help='print masked transcript and answer key')
    args = parser.parse_args()
    text = Path(args.file).read_text(encoding='utf-8')
    if args.blind:
        masked, key = blind(text)
        print(json.dumps({'masked': masked, 'key': key}, ensure_ascii=False, indent=2))
    else:
        print(json.dumps(stats(text), ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
