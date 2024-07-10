from tkinter import *

TITLE = "Distance Converter"
CONVERSION_FACTOR = 1.609

window = Tk()

window.config(width=600, height=500, padx=50, pady=50)
window.title(TITLE)

label = Label(text="Distance Converter", font=("Helvetica", 24, "bold"))
km_label = Label(text="Km", font=("Helvetica", 24, "bold"))
miles_label = Label(text="Miles", font=("Helvetica", 24, "bold"))

km_input = Entry(width=20)
miles_input = Entry(width=20)

convert_button = Button(text="Convert", width=40)

label.grid(column=0, row=0)

km_input.grid(column=0, row=2)
miles_input.grid(column=1, row=2)

km_label.grid(column=0, row=1)
miles_label.grid(column=1, row=1)

convert_button.grid(column=0, row=3, columnspan=2)


def km_to_miles(km):
    return km * CONVERSION_FACTOR


def miles_to_km(miles):
    return miles / CONVERSION_FACTOR


def convert():
    input_miles = int(miles_input.get()) if miles_input.get() else 0
    input_km = int(km_input.get()) if km_input.get() else 0

    if input_km > 0:
        output_miles = km_to_miles(input_km)
        output_miles = round(output_miles, 2)
        miles_input.insert(END, str(output_miles))
    if input_miles > 0:
        output_km = miles_to_km(input_miles)
        output_km = round(output_km, 2)
        km_input.insert(END, str(output_km))


convert_button["command"] = convert

window.mainloop()
