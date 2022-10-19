from unittest import TestCase

from project_212 import calc


class TestProject212(TestCase):
    def test_calc(self) -> None:
        cases = [
            (3, (1, 2)),
            (0, (-1, 1)),
        ]
        for expected, args in cases:
            with self.subTest(expected):
                self.assertEqual(expected, calc(*args))
