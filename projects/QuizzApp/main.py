from html import unescape
from random import shuffle

from question_model import Question
from quiz_brain import QuizBrain
from trivia_client import OpenTriviaClient
from ui import QuizzInterface

client = OpenTriviaClient()

data = client.fetch_trivia(amount=100)
question_data = data["results"]

shuffle(question_data)

question_bank = []
for question in question_data:
    question_text = unescape(question["question"])
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

ui = QuizzInterface()
quiz = QuizBrain(question_bank, ui=ui)

quiz.start_quiz()
