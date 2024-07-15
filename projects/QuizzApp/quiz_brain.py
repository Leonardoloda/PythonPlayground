from ui import QuizzInterface


class QuizBrain:

    def __init__(self, q_list, ui: QuizzInterface):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = q_list[0]
        self.ui = ui

        self.ui.register_true_listener(self.answer_true)
        self.ui.register_false_listener(self.answer_false)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        if not self.still_has_questions():
            self.ui.disable_buttons()
            return self.ui.update_question("Game over")

        self.current_question = self.question_list[self.question_number]
        self.question_number += 1

        self.ui.update_question(self.current_question.text)

    def update_score(self, score):
        self.score += score
        self.ui.update_score(self.score)

    def answer_true(self):
        self.check_answer("true")

    def answer_false(self):
        self.check_answer("false")

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        self.ui.disable_buttons()

        if user_answer.lower() == correct_answer.lower():
            self.update_score(1)
            self.ui.show_correct()
        else:
            self.ui.show_wrong()

        self.ui.window.after(3000, self.next_question)
        self.ui.window.after(3000, self.ui.enable_buttons)

    def start_quiz(self):
        self.next_question()

        self.ui.window.mainloop()
