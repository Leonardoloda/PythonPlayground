class Host:
    def __init__(self, questions):
        self.questions = questions
        self.current_question = None
        self.score = 0

    def increase_score(self, score=1):
        self.score += score

    def start_game(self):
        print(f"Welcome to your game, time to start the first of {len(self.questions)} \n")
        self.current_question = 0

    def end_game(self):
        print("Thank you for playing!")
        print(f"Your final score is {self.score} out of {len(self.questions)}")

    def ask_question(self):
        user_answer = input(f"{self.questions[self.current_question].question} (True/False): ")

        is_correct = self.check_answer(user_answer=user_answer,
                                       real_answer=self.questions[self.current_question].answer)

        if is_correct:
            print("Correct! You got it right")
            self.increase_score()
        else:
            print("Wrong! You got it wrong")

    def check_answer(self, user_answer, real_answer):
        return user_answer == real_answer

    def has_more_questions(self):
        return self.current_question < len(self.questions)

    def next_question(self):
        print(f"Currently you're at question {self.current_question + 1}")
        print(f"Your current score is {self.score}/{len(self.questions)}")
        print(f"Ready for you next question \n\n")
        self.current_question += 1
