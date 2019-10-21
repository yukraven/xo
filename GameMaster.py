# coding: utf8
class GameMaster:
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
