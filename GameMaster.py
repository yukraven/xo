# coding: utf8
from enum import Enum


class Wait(Enum):
    question = 1
    any_question = 2
    answer = 3


class GameMaster:
    """ Игровой клиент, отвечает за все взаимодействия с игрой """
    hi_list = ["привет"]

    state = Wait.answer
    question = "Хочешь сыграть?"
    question_owner = 0
    answer = "да"
    answer_owner = 0

    return_dict = {Wait.answer: "Привет! Состояние - ожидаем ответ. Текущий вопрос - ",
                   Wait.question: "Привет! Состояние - ожидаем вопрос от ответившего.",
                   Wait.any_question: "Привет! Состояние - ожидаем вопрос от любого игрока."}

    def entryPoint(self, text, user_id):
        text = text.lower()
        words_list = text.split(" ")

        if words_list[0] in self.hi_list:
            result = self.return_dict[self.state]
            if self.state == Wait.answer:
                result += self.question
            return result



    """
    state = "answerWaiting"
    question = "Хочешь сыграть?"
    questionOwner = 0
    answer = "да"
    answerOwner = 0
    players = {}

    def sendMessage(self, message, user_id):
        print("id: %s, message: %s, state: %s" % (user_id, message, self.state))
        if message.lower() == "топ":
            return str(self.players)
        elif message.lower() == "счет":
            try:
                temp = self.players[user_id]
            except:
                temp = 0
            return temp
        elif self.state == "answerWaiting":
            if user_id == self.questionOwner:
                return "Ты не можешь ответить на собственный вопрос."
            elif message.lower() == self.answer:
                print("get correct answer")
                try:
                    self.players[user_id] += 1
                except:
                    self.players[user_id] = 1
                self.answerOwner = user_id
                self.state = "questionWaiting"
                return "Правильно! +1 балл! А теперь напиши свои вопрос и ответ через троеточие (...)."
            else:
                return "Неправильно! Попробуй еще раз. Вопрос звучит так: %s" % self.question
        elif self.state == "questionWaiting":
            if self.answerOwner == 0 or self.answerOwner == user_id:
                if message.count("...") == 1:
                    temp = message.split("...")
                    self.question = temp[0].strip().lower()
                    self.answer = temp[1].strip().lower()
                    self.questionOwner = user_id
                    self.state = "answerWaiting"
                    print("new question: %s, answer: %s" % (self.question, self.answer))
                    return "Вопрос принят! Жди, пока на него ответят."
                else:
                    return "Неправильно записан вопрос. Напиши свои вопрос и ответ через троеточие (...)."
            else:
                return "Другой человек задает вопрос. Жди."
                """
