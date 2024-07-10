# Tkniter allows us to create uis
from tkinter import *

window = Tk()

# We can change the window taittle
window.title("Hello World")

# Set up a minimum size for the window
window.minsize(width=300, height=500)

# padding can be added around each element
window.config(padx=50, pady=50)

# Create labels
custom_label = Label(window, text="My first label", font=("Helvetica", 20, "bold"))

# We can pass options to locate the element
custom_label.pack()

custom_label["text"] = "My second label"
custom_label.config(text="My third label")

# You can laso use it to craete button
button = Button(text="Click me")
# You can use place to set any coordinate
button.place(x=0, y=0)

# Create inputs
input = Entry(width=100)
input.insert(0, string="Initial text")
input.pack()


def enter_message():
    custom_label["text"] = input.get()


button["command"] = enter_message

# Text areas by setting number of lines with height
text_area = Text(height=5, width=100)
text_area.focus()
text_area.insert(END, "My first text")
text_area.pack()

print(text_area.get("1.0", END))


# spinbox
def on_change():
    print(spinbox.get())


spinbox = Spinbox(from_=1900, to=2024, width=5, command=on_change)
spinbox.pack()


# Scale
def on_scale_change(value):
    print(value)


scale = Scale(from_=0, to=100, command=on_scale_change)
scale.pack()


# Checkbutton
def on_clicked():
    # Prints a boolean based on the state
    print(checked_state.get())


# variable to hold on to checked state, 0 is off, 1 is on.
checked_state = BooleanVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=on_clicked)
checkbutton.pack()


# Radiobutton
def on_value_change():
    print(radio_state.get())


# Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=on_value_change)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=on_value_change)
radiobutton1.pack()
radiobutton2.pack()


# Listbox
def listbox_used(event):
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

window.mainloop()
