from unittest import TestCase

from nastya_bot import command_answer
from nastya_bot import generate_advice
from nastya_bot import first
from nastya_bot import second
from nastya_bot import third
from nastya_bot import second_add


class TestNastyaBot(TestCase):
    def test_commands(self) -> None:
        cases = [
            ("Hi! I can tell you your horoscope for today", "/start"),
            ("This bot can predict your horoscope for today. To get started, write /start", "/help"),
            ("I don't understand you. Please write /help.", "bla bla bla")
        ]
        for expected, args in cases:
            with self.subTest(expected):
                self.assertEqual(expected, command_answer(args))

    def test_advice(self) -> None:
        advices_list = first + second + second_add + third
        check_if_contains = any(substring in generate_advice() for substring in advices_list)
        self.assertTrue(check_if_contains)

