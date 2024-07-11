# Only import classes
from tkinter import *
from tkinter import messagebox

from pyperclip import copy

from generator import Generator
from repository import Repository

window = Tk()

WHITE = "#FBFEF9"
BLACK = "#000004"
PURPLE = "#7E1946"

WIDTH = 600
HEIGHT = 500
PADDING = 50

TITLE = 'Password Generator'

PATH = "files/record.csv"

generator = Generator()
repository = Repository(path=PATH)

window.title(TITLE)
window.config(pady=PADDING, padx=PADDING, width=WIDTH, height=HEIGHT, bg=WHITE)

canvas = Canvas(background=WHITE, width=200, height=200, bg=WHITE, highlightthickness=0)
logo = PhotoImage(file="assets/logo.png")

canvas.create_image(100, 100, image=logo, )

website_label = Label(text="Website: ", bg=WHITE, fg=BLACK, font=("Helvetica", 20))
email_label = Label(text="Email: ", bg=WHITE, fg=BLACK, font=("Helvetica", 20))
password_label = Label(text="Password: ", bg=WHITE, fg=BLACK, font=("Helvetica", 20))

website_input = Entry(width=35, bg=WHITE, fg=BLACK, highlightthickness=0)
email_input = Entry(width=35, bg=WHITE, fg=BLACK, highlightthickness=0)
password_input = Entry(width=21, bg=WHITE, fg=BLACK, highlightthickness=0)


def create_password():
    generated_password = generator.generate_password()

    password_input.insert(END, generated_password)

    copy(generated_password)


def save_password():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    if not website or not email or not password:
        messagebox.showerror(title="Error", message="Please enter all fields")
        return

    repository.add_website(website=website, email=email, password=password)

    messagebox.showinfo("Success", "Password has been saved")

    website_input.delete(0, END)
    email_input.delete(0, END)
    password_input.delete(0, END)


generate_button = Button(text="Generate", bg=PURPLE, fg=BLACK, highlightthickness=0, width=10, highlightcolor=PURPLE,
                         command=create_password)
add_button = Button(text="Add Password", width=32, bg=PURPLE, fg=BLACK, highlightthickness=0, command=save_password)

canvas.grid(row=0, column=0, columnspan=3)

website_label.grid(row=1, column=0)
website_input.grid(row=1, column=1, columnspan=2)

email_label.grid(row=2, column=0)
email_input.grid(row=2, column=1, columnspan=2)

password_label.grid(row=3, column=0)
password_input.grid(row=3, column=1)
generate_button.grid(row=3, column=2)

add_button.grid(row=4, column=1, columnspan=2)

email_input.insert(END, "mail@mail.com")
website_input.focus()

window.mainloop()
