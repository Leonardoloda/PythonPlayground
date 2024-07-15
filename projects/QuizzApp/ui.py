from tkinter import *


class QuizzInterface:
    THEME_COLOR = "#375362"

    def __init__(self):
        self.window = Tk()

        self.window.title("Quizz")
        self.window.config(width=600, height=900, padx=15, pady=15, bg=self.THEME_COLOR)

        self.score = Label(text="Score: 0", bg=self.THEME_COLOR, fg="white", font=("Courier", 20), pady=20)

        self.canvas = Canvas(width=400, height=400, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(200, 200, text="Question", font=("Courier", 20, "italic"),
                                                     width=200)

        self.true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.true_image, highlightthickness=0, pady=20)

        self.false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false_image, highlightthickness=0, pady=20)

        self.score.grid(row=0, column=1, columnspan=2)
        self.canvas.grid(row=1, column=0, columnspan=2)
        self.false_button.grid(row=2, column=0)
        self.true_button.grid(row=2, column=1)

    def register_true_listener(self, command):
        self.true_button.config(command=command)

    def register_false_listener(self, command):
        self.false_button.config(command=command)

    def update_score(self, score):
        self.score.config(text=f"Score: {score}")

    def update_question(self, question):
        self.canvas.config(bg="white")
        self.canvas.itemconfig(self.question_text, text=question, fill="black")

    def show_correct(self):
        self.canvas.config(bg="green")
        self.canvas.itemconfig(self.question_text, fill="white")

    def show_wrong(self):
        self.canvas.config(bg="red")
        self.canvas.itemconfig(self.question_text, fill="white")

    def enable_buttons(self):
        self.true_button.config(state="active")
        self.false_button.config(state="active")

    def disable_buttons(self):
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")
