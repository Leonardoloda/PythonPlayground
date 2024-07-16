from data import question_data
from host import Host
from question import Question

question_bank = []

for question in question_data:
    question_bank.append(Question(question["text"], question["answer"]))

host = Host(question_bank)

host.start_game()

while host.has_more_questions():
    answer = host.ask_question()

    host.next_question()

host.end_game()
