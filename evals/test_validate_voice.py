import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from validate import voice_errors  # noqa: E402

GOOD = """## 목소리

- 리듬: 문장 길이 — 보통 / 전개 — 원칙→사례→예외
- 설정값: 직설성 8 · 유머 6 · 친근함 7 · 감정 표현 3 · 도발성 4 · 질문 빈도 5
- 화법 장치: 비유 — 일상 비유 / 유머 — 자기 낮춤 / 강조 — 대비 / 설득 — 경험 / 말끝 — 한계로 끝냄
- 회의 반응: 새 아이디어 — 구조를 묻는다 / 반박할 때 — 조건을 따진다 / 비판받을 때 — 실수를 인정한다 / 모를 때 — 범위 밖이라고 말한다
- 확인된 짧은 공개 표현:
  - "Example phrase here." 번역: 예시 문장. 맥락: 시험용. ([출처](https://example.org/a))
- 하지 말 것: 투자 권유를 하지 않는다.
- 합성 대사 예시(합성): 하나만 먼저 물을게요.

## 잘 맞는 질문
"""

NO_QUOTES = GOOD.replace(
    '- 확인된 짧은 공개 표현:\n  - "Example phrase here." 번역: 예시 문장. 맥락: 시험용. ([출처](https://example.org/a))\n',
    '- 확인된 짧은 공개 표현: 없음\n',
)

ITEM = '  - "Example phrase here." 번역: 예시 문장. 맥락: 시험용. ([출처](https://example.org/a))\n'


class VoiceErrors(unittest.TestCase):
    def test_good_section_passes(self):
        self.assertEqual(voice_errors(GOOD), [])

    def test_missing_section(self):
        self.assertEqual(voice_errors('## 출처\n'), ['missing 목소리 section'])

    def test_missing_field(self):
        body = GOOD.replace('- 하지 말 것: 투자 권유를 하지 않는다.\n', '')
        self.assertIn('missing field: 하지 말 것', voice_errors(body))

    def test_setting_out_of_range(self):
        self.assertIn('invalid setting: 유머', voice_errors(GOOD.replace('유머 6', '유머 11')))

    def test_missing_setting(self):
        self.assertIn('invalid setting: 도발성', voice_errors(GOOD.replace(' · 도발성 4', '')))

    def test_none_quotes_pass(self):
        self.assertEqual(voice_errors(NO_QUOTES), [])

    def test_quote_needs_https_source(self):
        body = GOOD.replace('([출처](https://example.org/a))', '(출처)')
        self.assertTrue(any('https' in e for e in voice_errors(body)))

    def test_at_most_three_quotes(self):
        body = GOOD.replace(ITEM, ITEM * 4)
        self.assertIn('quotes must be 없음 or 1-3 items', voice_errors(body))

    def test_reaction_keys_required(self):
        body = GOOD.replace(' / 모를 때 — 범위 밖이라고 말한다', '')
        self.assertIn('missing reaction: 모를 때', voice_errors(body))


if __name__ == '__main__':
    unittest.main()
