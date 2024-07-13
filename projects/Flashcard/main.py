from tkinter import *

from constants import *
from csv_repository import CSVRepository

screen = Tk()
repo = CSVRepository(path=FILE_PATH)

screen.config(background=BACKGROUND_COLOR, width=SCREEN_WIDTH, height=SCREEN_HEIGHT, padx=PAD_X, pady=PAD_Y)
screen.title(TITLE)

word = repo.get_word()
flip = None

card_canvas = Canvas(width=CARD_WIDTH, height=CARD_HEIGHT, bg=BACKGROUND_COLOR, highlightthickness=0)

front_image = PhotoImage(file=FRONT_IMAGE_PATH)
back_image = PhotoImage(file=BACK_IMAGE_PATH)
right_image = PhotoImage(file=RIGHT_IMAGE_PATH)
wrong_image = PhotoImage(file=WRONG_IMAGE_PATH)

card_bg = card_canvas.create_image(CARD_WIDTH / 2, CARD_HEIGHT / 2, image=front_image)
super_title_text = card_canvas.create_text(CARD_WIDTH / 2, CARD_HEIGHT / 2 - 100, text="", font=SUPER_TITLE_FONT)
title_text = card_canvas.create_text(CARD_WIDTH / 2, CARD_HEIGHT / 2, text="", font=TITLE_FONT)


def flip_card():
    global word

    card_canvas.itemconfig(card_bg, image=back_image)

    card_canvas.itemconfig(super_title_text, text="French")
    card_canvas.itemconfig(title_text, text=word.French)


def next_word():
    global word, flip

    if flip:
        screen.after_cancel(flip)

    new_word = repo.get_word()

    card_canvas.itemconfig(card_bg, image=front_image)

    card_canvas.itemconfig(super_title_text, text="English")
    card_canvas.itemconfig(title_text, text=new_word.English)

    flip = screen.after(5000, flip_card)

    word = new_word


def right():
    global word

    repo.check_word(word.French)

    next_word()


right_button = Button(width=RIGHT_WIDTH, height=RIGHT_HEIGHT, image=right_image, highlightthickness=0, command=right)
wrong_button = Button(width=WRONG_WIDTH, height=WRONG_HEIGHT, image=wrong_image, highlightthickness=0,
                      command=next_word)

right_button.grid(row=1, column=0)
wrong_button.grid(row=1, column=1)
card_canvas.grid(row=0, column=0, columnspan=2)

next_word()

screen.mainloop()
