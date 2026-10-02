"""Check skill references, extensible catalogs, and command composition invariants."""
import json
import re
from pathlib import Path
from commands import resolve

ROOT = Path(__file__).resolve().parents[1]
ROLES = {'Visionary','Operator','Investor','ProductThinker','Contrarian','CustomerAdvocate','Ethicist'}
SECTIONS = ['확인한 공개 표현','공개적으로 확인 가능한 핵심 철학','사고 프레임','의사결정 기준','목소리','잘 맞는 질문','잘 맞지 않는 질문','피해야 할 과장','대표적인 관점','출처']
VOICE_FIELDS = ['리듬','설정값','화법 장치','회의 반응','확인된 짧은 공개 표현','하지 말 것','합성 대사 예시']
VOICE_SETTINGS = ['직설성','유머','친근함','감정 표현','도발성','질문 빈도']
VOICE_REACTIONS = ['새 아이디어','반박할 때','비판받을 때','모를 때']
FENCE = re.compile(r'^(```|~~~).*?^\1[^\n]*$', re.M | re.S)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def safe_path(rel):
    target = (ROOT / rel).resolve()
    require(ROOT in target.parents, f'Catalog path escapes skill: {rel}')
    require(target.is_file(), f'Missing file: {rel}')
    return target


def section(body, title):
    match = re.search(rf'^## {re.escape(title)}[^\n]*\n(.*?)(?=^## |\Z)', body, re.M | re.S)
    return match.group(1) if match else ''


def voice_errors(body):
    """Return problems in a profile's 목소리 section; an empty list means valid."""
    voice = section(body, '목소리')
    if not voice:
        return ['missing 목소리 section']
    errors = []
    for field in VOICE_FIELDS:
        if not re.search(rf'^- {re.escape(field)}(?:\([^)]*\))?:', voice, re.M):
            errors.append(f'missing field: {field}')
    settings = re.search(r'^- 설정값:(.*)$', voice, re.M)
    if settings:
        found = {k.strip(): int(v) for k, v in re.findall(r'([가-힣 ]+?)\s*(\d+)', settings.group(1))}
        for key in VOICE_SETTINGS:
            if not 0 <= found.get(key, -1) <= 10:
                errors.append(f'invalid setting: {key}')
    reactions = re.search(r'^- 회의 반응:(.*)$', voice, re.M)
    if reactions:
        for key in VOICE_REACTIONS:
            if f'{key} —' not in reactions.group(1):
                errors.append(f'missing reaction: {key}')
    quotes = re.search(r'^- 확인된 짧은 공개 표현:(.*?)(?=^- |\Z)', voice, re.M | re.S)
    if quotes:
        head, _, rest = quotes.group(1).partition('\n')
        items = re.findall(r'^\s+- (.+)$', rest, re.M)
        if head.strip() == '없음':
            if items:
                errors.append('quotes marked 없음 but items listed')
        elif not 1 <= len(items) <= 3:
            errors.append('quotes must be 없음 or 1-3 items')
        for item in items:
            if not re.search(r'"[^"]+"', item) or '](https://' not in item:
                errors.append(f'quote needs "text" and https source: {item[:30]}')
    return errors


def validate():
    skill = (ROOT / 'SKILL.md').read_text(encoding='utf-8')
    require(skill.startswith('---\nname: celebrity-panel\ndescription:'), 'Invalid entrypoint identity')
    require('references/dialogue.md' in skill, 'SKILL.md must link references/dialogue.md')
    people = json.loads((ROOT / 'people/catalog.json').read_text(encoding='utf-8'))['people']
    modes = json.loads((ROOT / 'modes/catalog.json').read_text(encoding='utf-8'))['modes']
    require(len(people) >= 10, 'At least ten example people required')
    require(len({p['id'] for p in people}) == len(people), 'Duplicate person IDs')
    require(len({p['name'] for p in people}) == len(people), 'Duplicate person names')
    for p in people:
        require(re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', p['id']), f'Invalid person ID: {p["id"]}')
        require(p['domains'] and p['roles'] and p['signature_question'], f'Incomplete selection data: {p["id"]}')
        require(set(p['roles']) <= ROLES, f'Unknown role: {p["id"]}')
        body = safe_path(p['path']).read_text(encoding='utf-8')
        require(all(section in body for section in SECTIONS), f'Incomplete profile: {p["id"]}')
        require('https://' in body, f'Missing public source: {p["id"]}')
        problems = voice_errors(body)
        require(not problems, f'Invalid voice in {p["id"]}: {problems}')
    commands = [c for m in modes for c in m['commands']]
    require(len(commands) == len(set(commands)), 'Ambiguous command alias')
    require(len({m['id'] for m in modes}) == len(modes), 'Duplicate mode IDs')
    for m in modes:
        require(m['kind'] in {'primary','modifier'}, f'Invalid mode kind: {m["id"]}')
        safe_path(m['path'])
    require({m['id'] for m in modes if m['kind']=='modifier'} == {'wildcard','random'}, 'Incorrect modifier set')
    registered_profiles = {safe_path(p['path']) for p in people}
    actual_profiles = set((ROOT / 'people').glob('*.md')) - {ROOT / 'people/index.md'}
    require(registered_profiles == actual_profiles, 'Unregistered or missing person profile')
    registered_modes = {safe_path(m['path']) for m in modes if m['path'].startswith('modes/')}
    require(registered_modes == set((ROOT / 'modes').glob('*.md')), 'Unregistered or missing mode')

    # Local Markdown links must resolve even after moving the whole directory.
    for file in ROOT.rglob('*.md'):
        if any(part.startswith('.') for part in file.relative_to(ROOT).parts):
            continue
        text = FENCE.sub('', file.read_text(encoding='utf-8'))
        for link in re.findall(r'\]\(([^)]+)\)', text):
            if link.startswith(('https://','http://','#')):
                continue
            target = (file.parent / link.split('#')[0]).resolve()
            require(target.exists(), f'Broken link in {file.relative_to(ROOT)}: {link}')
    return people, modes, commands


def command_checks():
    cases = [
        ('$celebrity-panel /meeting /wildcard 블로그 사업', ['meeting'], ['wildcard'], False),
        ('/celebrity-panel /postmortem /pivot /jury /wildcard 서비스', ['postmortem','pivot','jury'], ['wildcard'], False),
        ('/random /wildcard /decision A와 B', ['decision'], ['random','wildcard'], False),
        ('/comment 오늘 첫 버전 완성', ['mentor'], [], False),
        ('/mentor 오늘 첫 버전 완성', ['mentor'], [], False),
        ('/wildcard 사업 아이디어', [], ['wildcard'], False),
        ('/ask /wildcard 미야자키만', ['single'], ['wildcard'], True),
        ('/ask /meeting 잡스만', ['single','meeting'], [], True),
        ('/jury /jury 자료', ['jury'], [], False),
        ('문자열 `/pivot`을 설명해줘', [], [], False),
        ('https://example.org/pivot', [], [], False),
        ('/meeting /api/v1 엔드포인트', ['meeting'], [], False),
    ]
    for text, pipeline, modifiers, conflict in cases:
        plan = resolve(text)
        require(plan['pipeline']==pipeline and plan['modifiers']==modifiers and plan['needs_single_panel_clarification']==conflict, f'Unexpected plan: {text}')
    require(resolve('/jury')['needs_problem_or_context'], 'Missing subject must be exposed')
    try:
        resolve('/unknown 대상')
    except ValueError:
        pass
    else:
        raise ValueError('Unknown commands must not silently choose a mode')
    return len(cases)+2


if __name__ == '__main__':
    people, modes, commands = validate()
    checks = command_checks()
    print(json.dumps({'people':len(people),'mode_files':len(list((ROOT/'modes').glob('*.md'))),'commands':len(commands),'composition_checks':checks,'local_links':'passed'},ensure_ascii=False))
