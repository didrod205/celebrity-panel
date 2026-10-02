# Celebrity Panel

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Sponsor](https://img.shields.io/badge/Sponsor-GitHub-db61a2?logo=githubsponsors&logoColor=white)](https://github.com/sponsors/didrod205)

고민, 아이디어, 사업 계획, 선택지를 **유명인 가상 패널**이 서로 다른 관점으로 검토하는 [Claude Code](https://claude.com/claude-code)·Codex 스킬입니다. 버핏은 되돌릴 수 없는 손실을, 봉준호는 실제 장면을, 파인만은 반증할 관찰을 묻는 식입니다. 응원이나 박수로 끝나지 않습니다. 답변에는 쟁점과 이견, 조건별 결론, 바로 해볼 수 있는 가장 작은 실험이 남습니다. 패널은 회의록 형식으로 서로 끼어들고 반박하며, 인물마다 근거 있는 말투가 다르게 들립니다.

```text
/celebrity-panel /meeting /wildcard 블로그 글을 자동으로 써주고 예약 발행까지 해주는 1인 창업 SaaS를 검토해줘.
```

> 공개 자료에서 영감받은 가상 패널입니다. 실제 인물의 발언이나 지지가 아닙니다.
> 모든 답변은 이 문장으로 시작합니다. 패널의 대사는 합성이며, 출처를 확인한 짧은 표현만 각주와 함께 등장합니다.

[English summary below.](#english)

---

## 무엇을 하나

- **15개 모드와 2개 구성 변경자.** 고민 상담, 아이디어 회의, 레드팀, A/B 결정, 멘토 댓글, 사업 심사, 고객 시뮬레이션, 가정 실패 회고(`/postmortem`), 피벗 3안(`/pivot`), 고객 공개 준비도 심사(`/jury`) 등을 지원합니다. 다른 분야 인물 한 명을 넣는 `/wildcard`와 예상 밖의 구성을 고르는 `/random`도 있습니다.
- **인물 33명.** 한국, 일본, 중국, 인도, 남아공, 유럽, 미주 등 여러 지역의 기업가, 감독, 운동선수, 과학자, 정치인, 예술가가 들어 있습니다. 인물마다 공개 자료 출처와 핵심 검토 질문이 프로필로 정리되어 있습니다.
- **사람처럼 말하는 회의록.** 인물 프로필마다 말 리듬, 직설성·유머 같은 설정값(말투를 잡기 위한 주관적 기본값이며 인물 평가가 아닙니다), 화법 장치, 확인된 짧은 공개 표현이 정리되어 있어 이름을 가려도 누가 말했는지 짐작할 수 있게 씁니다. 회의 끝에 패널이 질문을 던지고, 답하면 같은 패널로 2라운드가 이어집니다.
- **명령 조합.** `/postmortem /pivot /jury`처럼 이어 쓰면 실패 원인을 찾고, 그 원인으로 대안 3개를 만들고, 각 대안의 공개 준비도까지 순서대로 검토합니다.
- **명령 없이도 동작합니다.** "회사에 남을까 사업을 시작할까? 유명인 패널로 짧게."처럼 말하면 목적에 맞는 모드를 스스로 고르고, 고른 이유를 한 줄로 알려줍니다.

## 지키는 원칙

가상 패널이라는 형식이 그럴듯한 거짓말이 되지 않도록 스킬에 규칙을 넣었습니다.

- 인물의 실제 표현은 프로필에 출처와 함께 등록된 짧은 표현만 각주를 달아 씁니다. 지어낸 명언, 경험담, 현재 견해를 만들지 않고 억양이나 번역체를 흉내 내지 않습니다.
- 고객 조사, 시장 수치, 사용자 반응을 만들어내지 않습니다. 합성 고객은 가정이라고 표시하고, 아직 측정하지 않은 숫자는 **제안값**으로 표시합니다.
- 최신 가격, 경쟁 제품, 법규는 웹 도구로 확인해 링크합니다. 확인하지 못한 범위는 따로 밝힙니다.
- 인물 수나 억지 합의로 결론을 내지 않습니다. 이견은 남기고 결론은 조건별로 씁니다.
- `/jury`에서는 근거가 없으면 가정으로 통과시키지 않고 **보류**합니다. 허위 주장 같은 문제는 평균 점수로 상쇄하지 않습니다.
- 전문 분야 밖에 적용할 때는 비유라고 밝히고, 법률, 의료, 투자 판단을 인물의 권위로 확정하지 않습니다.

## 답변 예시

명령 없이 `회사에 남을까 사업을 시작할까? 유명인 패널로 짧게.`라고 입력했을 때 실제로 생성된 답변의 앞부분입니다. 고지 문장과 회의록의 처음 6턴이고, 대사 끝의 [1], [2]는 각주 번호입니다.

> 공개 자료에서 영감받은 가상 패널입니다. 실제 인물의 발언이나 지지가 아닙니다.
>
> ## 회의록
>
> **진행자** 오늘 안건은 회사에 남을지, 사업을 시작할지입니다. 사업 아이템과 자금 사정은 아직 모른다고 가정하고 버핏 님부터 시작하겠습니다.
>
> **버핏** 저라면 손실부터 봅니다. 먼저 숫자 두 개만 알고 싶어요. 월급 없이 몇 달을 버틸 수 있는지, 그리고 사업이 안 됐을 때 돌아갈 길이 있는지요. 이 두 숫자를 모르면 아직은 제가 이해할 수 있는 결정이 아닙니다.
>
> **나발** 저는 질문부터 다시 정의하고 싶어요. 회사냐 사업이냐가 아니라, 내가 쌓은 지식이 지금 누구의 자산을 키우고 있느냐입니다. 회사에서 배운 걸 내 이름으로 팔 수 있으면 그건 사업의 재료이고, 팔 수 없으면 아직 재료가 없는 겁니다.
>
> **이치로** 사업을 하고 싶다는 건 아직 꿈에 가깝습니다. 꿈꾸는 건 즐겁지만 목표는 어렵고 도전적이에요.[1] 이번 주 퇴근 후 몇 시에 무엇을 할지 정하지 못했다면 아직 목표가 아닙니다.
>
> **파인만** 하나 물어볼게요. 사업이 좋아서 가고 싶은 건가요, 아니면 회사가 싫어서 사업이 좋아 보이는 건가요? 스스로를 속이지 말아야 하고, 가장 속이기 쉬운 사람이 바로 자기 자신이에요.[2] 회사가 싫은 게 이유라면 이직도 같은 후보 목록에 올려야 공정한 비교가 됩니다.
>
> **나발** 버핏 님 말씀에는 반만 동의해요. 안전장치는 필요하지만, 회사에 남는 것도 공짜는 아닙니다. 지금 일이 시간을 팔아서 버는 구조라면 거기에 오래 머무는 것도 비용이에요.
>
> (...)

전체 답변은 [03-advice-no-command.md](docs/examples/03-advice-no-command.md)에 있고, 예시 7건은 [docs/examples](docs/examples/README.md)에 있습니다. 회의, 실패 회고에서 피벗과 공개 심사로 이어지는 조합, 상담, 조건 충돌 확인, 정치 인물 토론, 멘토 댓글, 2라운드를 각각 하나씩 담았습니다. 이 중 04(조건 충돌 확인)는 이전(2026-10-01) 형식으로 생성한 사례입니다.

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
| `/advice` | 고민·진로·관계 상담. 3~5명이 대화하며 조건별 판단을 줍니다. |
| `/meeting` | 구체적인 아이디어 회의. 진행자가 여는 회의록으로 첫 반응, 상호 반박, 쟁점과 개선안, 결론 순서로 이어집니다. |
| `/redteam` | 안 쓸 이유, 돈 안 낼 이유, 복제 가능성, 숨은 비용 등으로 아이디어를 공격합니다. |
| `/improve` | 한 줄 아이디어를 고객, 과업, 가치의 가설로 발전시킵니다. |
| `/decision` | A/B 선택. 기대효과, 리스크, 되돌릴 수 있는지 등으로 비교표를 만듭니다. |
| `/comment`, `/mentor` | 진행 상황에 댓글 스레드로 짧게 반응합니다. |
| `/reflection` | 실제로 겪은 일을 회고합니다. 사실과 해석을 구별합니다. |
| `/future` | 잘 풀림, 평범, 실패의 세 시나리오와 각각 관찰할 신호를 정리합니다. |
| `/invest` | 문제 크기, 지불 의사, 유통, 단위 경제성으로 사업을 심사합니다. |
| `/customer` | 특정 고객 유형을 합성 역할로 세워 사용 맥락을 검토합니다. |
| `/debate` | 주장의 찬반 논거와 반박을 대화로 주고받습니다. 실제 인물의 정치 입장은 부여하지 않습니다. |
| `/ask` | 지정한 인물 한 명과 1:1 대담을 합니다. |
| `/jury` | 지금 자료를 고객에게 공개해도 되는지 공개 가능, 조건부, 보류, 부적합으로 판정합니다. |
| `/postmortem` | 이미 실패했다고 가정하고 실패 경로, 조기 신호, 예방책을 찾습니다. |
| `/pivot` | 기존 자산을 살리는 서로 다른 사업 모델을 정확히 3개 제시합니다. |
| `/wildcard` | 주 모드에 결합합니다. 분야가 다른 인물을 정확히 1명 넣습니다. |
| `/random` | 주 모드에 결합합니다. 예상 밖의 패널 구성을 고릅니다. |

`짧게`, `댓글만`, `냉정하게`, `깊게`, `4명으로`, `파인만을 넣어줘` 같은 말로 길이, 톤, 인원, 인물을 조절할 수 있습니다. 모든 명령의 예시와 조합 규칙, 인물 목록은 **[사용법 문서](docs/USAGE.md)**에 있습니다.

## 검증

- **구조 검증.** 스킬 폴더에서 `python3 scripts/validate.py`를 실행합니다. 인물 33명과 `목소리` 섹션, 모드 파일 16개, 명령 18개, 명령 조합 14개 사례, 내부 링크를 검사합니다. 측정 도구와 검증기의 단위 테스트는 `python3 -m unittest discover -s evals -p 'test_*.py'`로 돌립니다. 답변 품질까지 보장하지는 않습니다.
- **실제 답변 생성 테스트 (2026-10-02).** 새 세션에서 스킬을 호출해 사례 6건과 재실행 2건을 만들고, `evals/transcript_stats.py`로 턴 수, 4문장을 넘는 턴, 정리 줄 수, 등록되지 않은 인용, 글자 수를 쟀습니다. 첫 실행에서 두 건이 분량 기준을 넘어 규칙을 고친 뒤 다시 돌렸고, 최종 답변 6건이 모두 통과했습니다. 다만 회의 예시(T1-r2)는 링크 주소를 포함해 5,548자로 제안값 5,000자를 548자 넘고, 화면에 보이는 글자는 4,735자입니다. 화자 이름을 가린 블라인드 말투 테스트의 정확도는 첫 실행 회의록이 90%, 재실행 회의록이 100%였습니다(기준 70%). 분량 초과를 포함한 측정표와 판정은 [evals/runs/2026-10-02/results.md](evals/runs/2026-10-02/results.md)에 있습니다.
- **이전 형식 테스트 (2026-10-01).** 회의록 형식으로 바꾸기 전에 Claude Code 4건과 Codex CLI 3건을 [행동 평가표](references/evaluation.md)로 채점했고 모두 통과했습니다. 새 형식은 Codex CLI에서 다시 돌리지 않았습니다.
- **알려진 한계.** 사례 6건과 재실행 2건, 모델 하나(Claude Opus)의 결과라 다른 모델이나 입력에서의 안정성은 확인하지 않았습니다. 답변 길이는 약 3,800~8,600자이고 여러 모드를 잇는 조합이 가장 깁니다. 댓글만 받으면 1,600자 안팎이고, `짧게`를 붙이면 회의록이 8~12턴으로 줄어듭니다. 턴 길이와 문장 수는 휴리스틱으로 세고, 블라인드 테스트는 서브에이전트 한 번의 추정입니다. 평가표 21개 사례 중 실제로 돌린 것은 일부입니다.

## 구조

```text
celebrity-panel/
├── SKILL.md               모델이 읽는 진입점: 모드 선택, 패널 구성, 출력 규칙
├── modes/                 모드별 진행 방식 16개 + catalog.json
├── people/                인물 프로필 33개 + index.md, catalog.json
├── references/            대화 규칙, 근거 원칙, 패널 선정, 예제, 확장 방법, 행동 평가표
├── templates/             출력 템플릿, 인물 프로필 템플릿
├── scripts/               commands.py (명령 정규화), validate.py (구조 검증)
├── agents/openai.yaml     Codex 표시 정보
├── evals/                 생성 답변 측정 도구와 테스트 기록
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

**Celebrity Panel** is a Claude Code and Codex skill that reviews your worries, ideas, plans, and choices through a virtual panel of public figures. Each panelist applies a thinking frame drawn from their public speeches, letters, and interviews, and every profile cites its sources. The panel doesn't stop at encouragement. It surfaces disagreements, gives conditional conclusions, and proposes the smallest experiment you can run next. Panels now talk as a meeting transcript, each with a sourced voice.

- **15 modes and 2 modifiers:** advice, meeting, red team, A/B decision, mentor comments, investment review, customer simulation, pre-mortem (`/postmortem`), three pivots (`/pivot`), launch-readiness jury (`/jury`), plus `/wildcard` (exactly one out-of-field panelist) and `/random`.
- **33 people** from Korea, Japan, China, India, South Africa, Europe, and the Americas.
- **Guardrails:** no fake quotes, no invented customer data or market numbers, unmeasured numbers labeled as proposals, and recent facts checked with web tools and linked. `/jury` holds a verdict when evidence is missing.
- **Output language:** the skill and its answers are in Korean.

```bash
git clone https://github.com/didrod205/celebrity-panel ~/.claude/skills/celebrity-panel
```

Then call it with `/celebrity-panel /meeting <your idea>` in Claude Code, or `$celebrity-panel ...` in Codex. Not affiliated with or endorsed by any person named. MIT licensed. [Sponsor on GitHub](https://github.com/sponsors/didrod205).
