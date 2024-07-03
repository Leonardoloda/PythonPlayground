class Question:

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def guess(self, answer):
        return self.answer == answer
