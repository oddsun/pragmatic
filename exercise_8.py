import re
import unittest

pattern = re.compile(r'(\d{1,2})(:(\d{2}))?(am|pm)?')


def parse(time):
    m = pattern.match(time)
    if m:
        hr, _, minute, postfix = m.groups()
        return int(hr or 0) * 60 + int(minute or 0) + (12 * 60 if postfix == 'pm' else 0)
    return 0


class TimeTest(unittest.TestCase):
    def setUp(self) -> None:
        self.test_cases = {
            '4:15am': 4 * 60 + 15,
            '4:15pm': 4 * 60 + 15 + 12 * 60,
            '4pm': 4 * 60 + 12 * 60,
            '4': 4 * 60,
            '4:15': 4 * 60 + 15,
        }

    def test_times(self):
        for time, minutes in self.test_cases.items():
            with self.subTest(time=time):
                self.assertEqual(parse(time), minutes)


if __name__ == '__main__':
    unittest.main()
