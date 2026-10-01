# 설치와 사용

이 폴더 전체가 재사용 단위다. `SKILL.md`만 복사하면 모드·인물 자료가 빠진다. 외부 패키지·API 키·MCP·서브에이전트가 필수는 아니다. Python 3은 선택적 명령 정규화·구조 검증에만 사용한다.

## Codex

개인 스킬 디렉터리 `~/.codex/skills/celebrity-panel/`에 전체 폴더를 둔다. 별도로 CODEX_HOME을 쓰는 환경에서는 그 경로의 `skills/`를 사용한다. 호출 예:

```text
$celebrity-panel /meeting /wildcard AI 블로그 서비스를 검토해줘.
$celebrity-panel /jury 이 랜딩페이지를 고객에게 공개해도 될까? [자료]
```

## Claude Code

개인 스킬은 `~/.claude/skills/celebrity-panel/`, 프로젝트 스킬은 `.claude/skills/celebrity-panel/`에 폴더 전체를 둔다. 호출 예:

```text
/celebrity-panel /meeting /wildcard AI 블로그 서비스를 검토해줘.
/celebrity-panel /postmortem /pivot 내 서비스가 실패했다고 가정해 대안을 찾아줘.
```

전체 폴더 심볼릭 링크도 Claude Code가 지원한다. 설치 위치와 `/skill-name` 호출 근거: [Claude Code 공식 Skills 문서](https://code.claude.com/docs/en/skills).

`/wildcard`, `/jury`, `/pivot` 등은 이 스킬의 내부 명령이며 각각 별개의 플랫폼 slash command로 등록되는 것은 아니다. 위처럼 스킬 호출 뒤에 붙인다. 자연어로 패널 회의를 요청해 자동 선택하게 할 수도 있다. Claude Code 로컬 설치가 Claude 웹·Cowork·클라우드 계정으로 자동 업로드되지는 않는다. 그 환경은 해당 제품의 스킬 추가 절차를 따른다.

## 조합·짧은 입력

```text
/meeting /wildcard /random 연차 추천 서비스를 만들고 싶어.
/postmortem /pivot /jury AI 콘텐츠 서비스의 다른 수익 구조를 찾아줘.
/ask 미야자키 하야오 관점만으로 제품 경험을 검토해줘.
/mentor 오늘 첫 버전을 만들었는데 방문자가 없어. 댓글만.
```

스킬을 활성화한 뒤 같은 대화에서는 이전 아이디어를 이어받아 `/pivot`처럼 짧게 요청할 수 있다. 다른 대화에서는 주제를 다시 제공한다. 주 모드는 명령 순서대로, wildcard·random은 구성 변경자로 적용한다.

## 선택적 도구

스킬 폴더에서:

```bash
python3 scripts/commands.py '/postmortem /pivot /jury /wildcard AI 콘텐츠 서비스'
python3 scripts/validate.py
```

명령 도구는 접두 명령만 정규화한다. 자연어 의미 분석·인물 추천·실제 패널 답변 생성기는 아니다. 모델은 `SKILL.md`와 관련 자료를 읽어 회의를 진행한다. 검증 도구는 파일과 명령 결합을 검사하며 답변 품질을 보장하지 않는다.
