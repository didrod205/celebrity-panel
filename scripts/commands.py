"""Normalize explicit skill commands; natural-language routing stays with the model."""
import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def resolve(text, root=ROOT):
    entries = json.loads((root / 'modes/catalog.json').read_text(encoding='utf-8'))['modes']
    commands = {c: m for m in entries for c in m['commands']}
    rest = text.strip()
    invocation = re.match(r'^(?:\$celebrity-panel|/celebrity-panel)(?=\s|$)', rest)
    if invocation:
        rest = rest[invocation.end():].lstrip()
    pipeline, modifiers, refs = [], [], []
    while True:
        match = re.match(r'^/([a-z][a-z0-9-]*)(?=\s|$)', rest)
        if not match:
            break
        command = match.group(1)
        if command not in commands:
            raise ValueError(f'Unknown panel command: /{command}')
        entry = commands[command]
        target = modifiers if entry['kind'] == 'modifier' else pipeline
        if entry['id'] not in target:
            target.append(entry['id'])
        if entry['path'] not in refs:
            refs.append(entry['path'])
        rest = rest[match.end():].lstrip()
    # Preserve command order; apply compositional constraints in the skill workflow.
    conflict = 'single' in pipeline and (len(pipeline) > 1 or 'wildcard' in modifiers)
    return {
        'pipeline': pipeline,
        'modifiers': modifiers,
        'problem': rest,
        'needs_auto_mode': not pipeline,
        'needs_problem_or_context': not rest,
        'needs_single_panel_clarification': conflict,
        'references': refs,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('text', help='Explicit command prefix and problem text')
    args = parser.parse_args()
    try:
        result = resolve(args.text)
    except ValueError as exc:
        parser.error(str(exc))
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
