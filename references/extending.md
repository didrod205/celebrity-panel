# 확장 방법

## 인물 추가

1. `templates/person-profile.md`를 `people/<id>.md`로 복사하고 실제 공개 자료로 채운다.
2. 전문 분야·자료 범위와 확인한 원칙, 새 질문에 응용한 해석을 분리한다. 원어 습관은 근거가 있을 때만 추가한다.
3. `people/catalog.json`에 `id`, `name`, `country`, `domains`, `roles`, `signature_question`, `path`, `evidence_scope`를 추가한다. 경로는 스킬 루트 기준 상대 경로다.
4. `people/index.md`에 링크를 추가한다. signature_question은 이미 있는 질문과 다른 전제를 검토해야 한다.
5. 구조 검증과 서로 다른 실제 입력을 시험한다. 유명인 이름을 지운 뒤에도 관점이 구별되는지 확인한다.

지원 역할은 Visionary, Operator, Investor, ProductThinker, Contrarian, CustomerAdvocate, Ethicist다. 새로운 역할을 도입하면 선정 가이드와 검증기의 허용 목록도 함께 갱신한다.

## 모드 추가

`modes/<mode>.md`에 목적, 입력, 진행, 필수 산출물, 근거의 한계를 적는다. `modes/catalog.json`에 고유한 `id`, `commands`, `kind`, `label`, `path`를 등록하고 `SKILL.md`의 자동 선택 표와 예제를 갱신한다. kind는 primary 또는 modifier다. 별칭끼리 충돌하면 안 된다.

결합 시 앞 결과를 어떻게 사용할지, 주 모드인지 구성 변경자인지, 한 명·인원 제약과 충돌할 때 무엇을 확인할지 정한다. 변경자 추가는 `scripts/validate.py`의 허용 변경자와 사례도 갱신한다.

## 검증

```bash
python3 scripts/validate.py
```

`references/evaluation.md`의 실제 프롬프트로 결과를 비교한다. 파일 검증 통과와 모델의 행동 검증은 별개다. 관찰한 실패에 맞춰 좁게 수정하고 새 사례를 추가한다. 설치 폴더가 복사본이면 원본 변경을 다시 복사하며, 심볼릭 링크면 원본 변경이 반영된다.
