# Celebrity Panel

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Sponsor](https://img.shields.io/badge/Sponsor-GitHub-db61a2?logo=githubsponsors&logoColor=white)](https://github.com/sponsors/didrod205)

고민, 아이디어, 사업 계획, 선택지를 **유명인 가상 패널**이 서로 다른 관점으로 검토하는 [Claude Code](https://claude.com/claude-code)·Codex 스킬입니다. 버핏은 되돌릴 수 없는 손실을, 봉준호는 실제 장면을, 파인만은 반증할 관찰을 묻는 식입니다. 응원이나 박수로 끝나지 않습니다. 답변에는 쟁점과 이견, 조건별 결론, 바로 해볼 수 있는 가장 작은 실험이 남습니다.

```text
/celebrity-panel /meeting /wildcard 블로그 글을 자동으로 써주고 예약 발행까지 해주는 1인 창업 SaaS를 검토해줘.
```

> 공개 자료에서 영감받은 가상 패널입니다. 실제 인물의 발언이나 지지가 아닙니다.
> 모든 답변은 이 문장으로 시작하며, 패널의 말은 실제 인용이 아닌 합성 코멘트로 표시됩니다.

[English summary below.](#english)

---

## 무엇을 하나

- **15개 모드와 2개 구성 변경자.** 고민 상담, 아이디어 회의, 레드팀, A/B 결정, 멘토 댓글, 사업 심사, 고객 시뮬레이션, 가정 실패 회고(`/postmortem`), 피벗 3안(`/pivot`), 고객 공개 준비도 심사(`/jury`) 등을 지원합니다. 다른 분야 인물 한 명을 넣는 `/wildcard`와 예상 밖의 구성을 고르는 `/random`도 있습니다.
- **인물 33명.** 한국, 일본, 중국, 인도, 남아공, 유럽, 미주 등 여러 지역의 기업가, 감독, 운동선수, 과학자, 정치인, 예술가가 들어 있습니다. 인물마다 공개 자료 출처와 핵심 검토 질문이 프로필로 정리되어 있습니다.
- **명령 조합.** `/postmortem /pivot /jury`처럼 이어 쓰면 실패 원인을 찾고, 그 원인으로 대안 3개를 만들고, 각 대안의 공개 준비도까지 순서대로 검토합니다.
- **명령 없이도 동작합니다.** "회사에 남을까 사업을 시작할까? 유명인 패널로 짧게."처럼 말하면 목적에 맞는 모드를 스스로 고르고, 고른 이유를 한 줄로 알려줍니다.

## 지키는 원칙

가상 패널이라는 형식이 그럴듯한 거짓말이 되지 않도록 스킬에 규칙을 넣었습니다.

- 인물의 말을 실제 인용처럼 쓰지 않고, 현재 견해나 지지를 지어내지 않습니다.
- 고객 조사, 시장 수치, 사용자 반응을 만들어내지 않습니다. 합성 고객은 가정이라고 표시하고, 아직 측정하지 않은 숫자는 **제안값**으로 표시합니다.
- 최신 가격, 경쟁 제품, 법규는 웹 도구로 확인해 링크합니다. 확인하지 못한 범위는 따로 밝힙니다.
- 인물 수나 억지 합의로 결론을 내지 않습니다. 이견은 남기고 결론은 조건별로 씁니다.
- `/jury`에서는 근거가 없으면 가정으로 통과시키지 않고 **보류**합니다. 허위 주장 같은 문제는 평균 점수로 상쇄하지 않습니다.
- 전문 분야 밖에 적용할 때는 비유라고 밝히고, 법률, 의료, 투자 판단을 인물의 권위로 확정하지 않습니다.

## 답변 예시

명령 없이 `회사에 남을까 사업을 시작할까? 유명인 패널로 짧게.`라고 입력했을 때 실제로 생성된 답변의 일부입니다.

> 공개 자료에서 영감받은 가상 패널입니다. 실제 인물의 발언이나 지지가 아닙니다.
>
> 진로 고민이라 **고민 상담 모드**로 진행합니다. 정답을 대신 고르기보다 손실, 장기 가치, 실행의 세 축으로 나눠 봅니다. (...)
>
> **워런 버핏에서 영감받은 관점 — Investor**
> 사업이 잘될지보다, 잘 안 됐을 때 되돌릴 수 없는 손실이 무엇인지부터 보세요. (...)
>
> **스즈키 이치로에서 영감받은 관점 — Operator**
> 퇴근 후 정해 둔 시간에 고객을 만나는 일을 지금 꾸준히 못 한다면, 퇴사한다고 그 시간이 저절로 생기지는 않습니다. (...)
>
> **가장 작은 실험** (숫자는 모두 제안값)
> 6주 동안 주 5시간을 들여 예상 고객 10명과 이야기하고, 선결제나 사전예약 같은 유료 반응을 직접 요청해 봅니다. (...) 유료 반응이 0건이면 아이템을 다시 검토하고, 3건 이상이면 퇴사 시점을 구체적으로 계획합니다.

전체 답변 4건은 [docs/examples](docs/examples/README.md)에 있습니다. 회의, 실패 회고에서 피벗과 공개 심사로 이어지는 조합, 상담, 조건 충돌 확인을 각각 하나씩 담았습니다.

## 설치

폴더 전체가 하나의 스킬입니다. `SKILL.md`만 복사하면 모드와 인물 자료가 빠지므로 저장소를 통째로 받아야 합니다. 필수 패키지, API 키, MCP는 없습니다.

**Claude Code** (모든 프로젝트에서 사용)

```bash
git clone https://github.com/didrod205/celebrity-panel ~/.claude/skills/celebrity-panel
```

특정 프로젝트에서만 쓰려면 그 프로젝트의 `.claude/skills/celebrity-panel`에 받습니다.

**Codex**

```bash
git clone https://github.com/didrod205/celebrity-panel ~/.codex/skills/celebrity-panel
```

`CODEX_HOME`을 따로 쓰면 그 경로 아래 `skills/`에 받습니다.

**둘 다 쓰는 경우.** 한 곳에 받고 심볼릭 링크를 걸면 수정 사항이 양쪽에 한 번에 반영됩니다.

```bash
git clone https://github.com/didrod205/celebrity-panel ~/celebrity-panel
```

```bash
ln -s ~/celebrity-panel ~/.claude/skills/celebrity-panel
```

```bash
ln -s ~/celebrity-panel ~/.codex/skills/celebrity-panel
```

**Claude 웹·데스크톱 앱.** 로컬에 설치한 스킬은 claude.ai 계정에 자동으로 올라가지 않습니다. [Releases](https://github.com/didrod205/celebrity-panel/releases/latest)에서 `celebrity-panel.zip`을 받아 앱 설정의 스킬 업로드 메뉴로 올립니다.

설치 뒤 스킬이 보이지 않으면 새 세션을 시작합니다. 업데이트는 받은 폴더에서 `git pull`로 합니다.

## 사용

```text
/celebrity-panel /meeting /wildcard AI 블로그 서비스를 검토해줘.
/celebrity-panel /postmortem /pivot /jury 소상공인 인스타그램 AI 구독 서비스. 아직 아이디어 단계야.
/celebrity-panel /decision 지금 이직할까, 1년 더 다닐까? 짧게.
/celebrity-panel /mentor 오늘 첫 버전 배포했는데 방문자가 0명이야. 댓글만.
/celebrity-panel /ask 미야자키 하야오 관점만으로 우리 앱 온보딩을 봐줘.
```

Codex에서는 `/celebrity-panel` 대신 `$celebrity-panel`로 부릅니다. `/meeting`, `/jury` 같은 명령은 따로 등록되는 슬래시 명령이 아니라 스킬 안에서 쓰는 명령이므로 스킬 이름 뒤에 붙입니다. 명령 없이 자연어로 요청해도 됩니다.

| 명령 | 하는 일 |
|---|---|
| `/advice` | 고민·진로·관계 상담. 3~5명이 각 2~4문장으로 조건별 판단을 줍니다. |
| `/meeting` | 구체적인 아이디어 회의. 첫 반응, 한 차례 상호 반박, 쟁점과 개선안, 결론 순서입니다. |
| `/redteam` | 안 쓸 이유, 돈 안 낼 이유, 복제 가능성, 숨은 비용 등으로 아이디어를 공격합니다. |
| `/improve` | 한 줄 아이디어를 고객, 과업, 가치의 가설로 발전시킵니다. |
| `/decision` | A/B 선택. 기대효과, 리스크, 되돌릴 수 있는지 등으로 비교표를 만듭니다. |
| `/comment`, `/mentor` | 진행 상황에 각 1~2문장의 짧은 멘토 댓글을 답니다. |
| `/reflection` | 실제로 겪은 일을 회고합니다. 사실과 해석을 구별합니다. |
| `/future` | 잘 풀림, 평범, 실패의 세 시나리오와 각각 관찰할 신호를 정리합니다. |
| `/invest` | 문제 크기, 지불 의사, 유통, 단위 경제성으로 사업을 심사합니다. |
| `/customer` | 특정 고객 유형을 합성 역할로 세워 사용 맥락을 검토합니다. |
| `/debate` | 주장의 찬반 논거와 반박. 실제 인물의 정치 입장은 부여하지 않습니다. |
| `/ask` | 지정한 인물 한 명의 관점만 봅니다. |
| `/jury` | 지금 자료를 고객에게 공개해도 되는지 공개 가능, 조건부, 보류, 부적합으로 판정합니다. |
| `/postmortem` | 이미 실패했다고 가정하고 실패 경로, 조기 신호, 예방책을 찾습니다. |
| `/pivot` | 기존 자산을 살리는 서로 다른 사업 모델을 정확히 3개 제시합니다. |
| `/wildcard` | 주 모드에 결합합니다. 분야가 다른 인물을 정확히 1명 넣습니다. |
| `/random` | 주 모드에 결합합니다. 예상 밖의 패널 구성을 고릅니다. |

`짧게`, `댓글만`, `냉정하게`, `깊게`, `4명으로`, `파인만을 넣어줘` 같은 말로 길이, 톤, 인원, 인물을 조절할 수 있습니다. 모든 명령의 예시와 조합 규칙, 인물 목록은 **[사용법 문서](docs/USAGE.md)**에 있습니다.

## 검증

- **구조 검증.** 스킬 폴더에서 `python3 scripts/validate.py`를 실행합니다. 인물 33명, 모드 파일 16개, 명령 18개, 명령 조합 14개 사례, 내부 링크를 검사합니다. 답변 품질까지 보장하지는 않습니다.
- **실제 답변 생성 테스트 (2026-10-01).** 각 사례를 새 세션에서 실행하고 [행동 평가표](references/evaluation.md)로 채점했습니다.
  - Claude Code 4건이 모두 통과했습니다. 회의와 wildcard, 실패 회고에서 피벗과 공개 심사로 이어지는 조합, 명령 없는 상담, 한 명 제약 충돌을 돌렸습니다.
  - Codex CLI 3건도 통과했습니다. 첫 실행에서 발견한 결함 두 가지를 고친 뒤 재시험한 결과입니다.
- **알려진 한계.** 회의나 여러 모드를 이어 쓰는 조합은 답변이 길어지는 편입니다. 6천~1만 3천 자까지 나왔습니다. 짧게 받으려면 `짧게`를 붙이세요. 평가표 16개 사례 중 실제로 돌린 것은 일부입니다.

## 구조

```text
celebrity-panel/
├── SKILL.md               모델이 읽는 진입점: 모드 선택, 패널 구성, 출력 규칙
├── modes/                 모드별 진행 방식 16개 + catalog.json
├── people/                인물 프로필 33개 + index.md, catalog.json
├── references/            근거 원칙, 패널 선정, 예제, 확장 방법, 행동 평가표
├── templates/             출력 템플릿, 인물 프로필 템플릿
├── scripts/               commands.py (명령 정규화), validate.py (구조 검증)
├── agents/openai.yaml     Codex 표시 정보
└── docs/                  사람이 읽는 사용법과 실제 답변 예시
```

모델은 `SKILL.md`를 읽은 뒤 고른 모드 파일과 선택한 인물 프로필만 추가로 읽습니다. 모든 자료를 한 번에 불러오지 않습니다.

## 인물·모드 추가

[확장 방법](references/extending.md)을 따릅니다. 인물은 `templates/person-profile.md`를 복사해 공개 자료로 채운 뒤 `people/catalog.json`과 `people/index.md`에 등록합니다. 모드는 `modes/catalog.json`과 `SKILL.md`의 선택 표에 함께 등록합니다. 수정한 뒤에는 `python3 scripts/validate.py`를 실행합니다.

## 후원

이 스킬이 결정을 한 번이라도 덜 후회하게 해줬다면 후원으로 유지보수를 응원해 주세요.

[![Sponsor on GitHub](https://img.shields.io/badge/Sponsor-GitHub-db61a2?logo=githubsponsors&logoColor=white)](https://github.com/sponsors/didrod205)

[GitHub Sponsors로 후원하기](https://github.com/sponsors/didrod205). 별(Star)도 다음 사람이 이 스킬을 찾는 데 도움이 됩니다.

## 고지

이 프로젝트는 여기에 등장하는 어떤 인물과도 관련이 없고, 그들의 승인이나 지지를 받지 않았습니다. 인물 프로필은 공개 연설, 서한, 인터뷰에서 확인한 사고 프레임을 요약하고 출처를 링크한 것입니다. 패널의 모든 코멘트는 모델이 생성한 합성 발언입니다. 답변은 검토와 제안일 뿐이며, 법률, 의료, 투자 자문이 아닙니다.

## License

[MIT](LICENSE)

---

## English

**Celebrity Panel** is a Claude Code and Codex skill that reviews your worries, ideas, plans, and choices through a virtual panel of public figures. Each panelist applies a thinking frame drawn from their public speeches, letters, and interviews, and every profile cites its sources. The panel doesn't stop at encouragement. It surfaces disagreements, gives conditional conclusions, and proposes the smallest experiment you can run next.

- **15 modes and 2 modifiers:** advice, meeting, red team, A/B decision, mentor comments, investment review, customer simulation, pre-mortem (`/postmortem`), three pivots (`/pivot`), launch-readiness jury (`/jury`), plus `/wildcard` (exactly one out-of-field panelist) and `/random`.
- **33 people** from Korea, Japan, China, India, South Africa, Europe, and the Americas.
- **Guardrails:** no fake quotes, no invented customer data or market numbers, unmeasured numbers labeled as proposals, and recent facts checked with web tools and linked. `/jury` holds a verdict when evidence is missing.
- **Output language:** the skill and its answers are in Korean.

```bash
git clone https://github.com/didrod205/celebrity-panel ~/.claude/skills/celebrity-panel
```

Then call it with `/celebrity-panel /meeting <your idea>` in Claude Code, or `$celebrity-panel ...` in Codex. Not affiliated with or endorsed by any person named. MIT licensed. [Sponsor on GitHub](https://github.com/sponsors/didrod205).
