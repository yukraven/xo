import unittest
from unittest import mock
from GameMaster import GameMaster
from GameMaster import Wait


class TestEntryPointGettingHi(unittest.TestCase):
    def setUp(self):
        self.GM = GameMaster()
        self.GM.question = "Вопрос"
        self.message = "привет"
        self.states = [Wait.question, Wait.any_question, Wait.answer]
        self.results = ["Привет! Состояние - ожидаем вопрос от ответившего.",
                        "Привет! Состояние - ожидаем вопрос от любого игрока.",
                        "Привет! Состояние - ожидаем ответ. Текущий вопрос - " + self.GM.question]

    def testState1(self):
        for i in range(3):
            with self.subTest(i=i):
                self.GM.state = self.states[i]
                result = self.GM.entryPoint(self.message, "")
                assert result == self.results[i]
