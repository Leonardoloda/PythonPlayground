from math import floor
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

stages = [
    {"label": "Work", "duration": WORK_MIN, "color": GREEN},
    {"label": "Break", "duration": SHORT_BREAK_MIN, "color": RED},
    {"label": "Work", "duration": WORK_MIN, "color": GREEN},
    {"label": "Break", "duration": SHORT_BREAK_MIN, "color": RED},
    {"label": "Work", "duration": WORK_MIN, "color": GREEN},
    {"label": "Break", "duration": SHORT_BREAK_MIN, "color": RED},
    {"label": "Work", "duration": WORK_MIN, "color": GREEN},
    {"label": "Break", "duration": LONG_BREAK_MIN, "color": PINK}
]

current_stage = 0
timer = None


def reset():
    global current_stage

    current_stage = 0
    screen.after_cancel(timer)

    title.config(text="Timer")

    canvas.itemconfig(timer_label, text=f"00:00")


def start_timer():
    global stages, current_stage

    if current_stage > len(stages) - 1:
        current_stage = 0

    stage_config = stages[current_stage]

    title["text"] = stage_config["label"]
    title.config(fg=stage_config["color"])
    decrease_counter(stage_config["duration"] * 60)


def decrease_counter(count):
    global current_stage, timer

    count_min = "{:02d}".format(floor(count / 60))
    count_sec = "{:02d}".format(floor(count % 60))

    canvas.itemconfig(timer_label, text=f"{count_min}:{count_sec}")

    if count > 0:
        timer = screen.after(1000, decrease_counter, count - 1)
    else:
        canvas.itemconfig(timer_label, text=f"{00}:{00}")

        current_stage += 1

        if current_stage % 2 != 0:
            checkmark.config(text="✅")

        timer = screen.after(1000, start_timer)
        start_timer()


screen = Tk()

screen.title("Pomodoro")
screen.config(background=YELLOW, width=500, height=400, padx=100, pady=100)

title = Label(text="Pomodoro", fg=GREEN, bg=YELLOW, font=("Timer", 60))
title.grid(column=1, row=0)

canvas = Canvas(background=YELLOW, width=200, height=224, highlightthickness=0)
photo = PhotoImage(file="assets/tomato.png")
canvas.create_image(100, 112, image=photo)
timer_label = canvas.create_text(100, 130, text="Pomodoro", fill="white", font=(FONT_NAME, 24, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

checkmark = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 24, "bold"))
checkmark.grid(column=1, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset)
reset_button.grid(column=2, row=2)

screen.mainloop()
