from turtle import Turtle, Screen

import pandas

turtle = Turtle()
screen = Screen()

screen.setup(width=800, height=500)
screen.bgpic(picname="assets/blank_states_img.gif")

turtle.penup()
turtle.hideturtle()

states_data = pandas.read_csv('files/50_states.csv')

states_count = states_data.state.count()

guesses = []

while len(guesses) < states_count:
    state_guess = screen.textinput(title=f"Guessed {len(guesses)}/50", prompt="Enter a new state")

    state_info = states_data[states_data.state == state_guess]

    if state_guess == "exit":
        break

    if state_info.empty:
        print("No a valid guess")
        continue

    state_x = float(state_info.x)
    state_y = float(state_info.y)
    guesses.append(state_guess)

    turtle.goto(x=state_x, y=state_y)
    turtle.write(state_guess, align="center", font=("Courier", 18))

remaining_states = states_data[~states_data.state.isin(guesses)]

remaining_states.to_csv("files/50_remaining_states.csv")
