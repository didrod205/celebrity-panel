import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from transcript_stats import blind, stats  # noqa: E402

ANSWER = """공개 자료에서 영감받은 가상 패널입니다. 실제 인물의 발언이나 지지가 아닙니다.

## 회의록

**진행자** 오늘 안건은 블로그 SaaS예요. 버핏 님부터요.

**버핏** 하나만 물을게요. 네이버가 막으면요? (웃으며) 저는 그게 제일 걸려요.

**나발** 버핏 님 걱정 맞아요. 그래도 해자는 업종 지식이에요. 첫째. 둘째. 셋째. 넷째.

**진행자** 정리하죠.

## 정리

- 합의: 플랫폼 위험이 크다.
- 이견: 해자의 위치.

## 각주

[1] 버핏 · "Registered line." — [출처](https://example.org/a)
[2] 나발 · "Invented line." — [출처](https://example.org/b)
"""

PROFILE = '## 목소리\n\n- 확인된 짧은 공개 표현:\n  - "Registered line." 번역: 등록. 맥락: 시험. ([출처](https://example.org/a))\n'


class TranscriptStats(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        (root / 'people').mkdir()
        (root / 'people' / 'warren-buffett.md').write_text(PROFILE, encoding='utf-8')
        self.result = stats(ANSWER, root)

    def tearDown(self):
        self.tmp.cleanup()

    def test_counts_turns_and_speakers(self):
        self.assertEqual(self.result['turns'], 4)
        self.assertEqual(self.result['speakers'], {'진행자': 2, '버핏': 1, '나발': 1})

    def test_flags_turns_over_four_sentences(self):
        self.assertEqual(self.result['long_turns'], [{'speaker': '나발', 'sentences': 6}])

    def test_counts_summary_lines(self):
        self.assertEqual(self.result['summary_lines'], 2)

    def test_checks_footnoted_quotes_against_profiles(self):
        self.assertEqual(self.result['cited_quotes'], ['Registered line.', 'Invented line.'])
        self.assertEqual(self.result['unregistered_quotes'], ['Invented line.'])

    def test_blind_masks_speakers_and_mentions(self):
        masked, key = blind(ANSWER)
        self.assertEqual(key, ['버핏', '나발'])
        self.assertIn('**화자 1** 하나만 물을게요.', masked)
        self.assertIn('**화자 2** ○○ 님 걱정 맞아요.', masked)
        self.assertIn('**진행자** 오늘 안건은 블로그 SaaS예요. ○○ 님부터요.', masked)

    def test_counts_comment_threads(self):
        text = '## 댓글\n\n**유재석** 첫 배포 축하해요.\n\n↳ **파인만** 근데 0명은 어떻게 셌어요?\n'
        self.assertEqual(stats(text, Path(self.tmp.name))['turns'], 2)


if __name__ == '__main__':
    unittest.main()
