from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)


def calculate():
    miles = float(miles_inp.get())
    km = round(miles * 1.609, int(decimal_places.get()))
    conversion_label.config(text=str(km))


# Widgets
km_label = Label(text="Km")
miles_label = Label(text="Miles")
equal_label = Label(text="is equal to")
conversion_label = Label(text="0")
calc_button = Button(text="Calculate", command=calculate)
miles_inp = Entry(width=10)
miles_inp.insert(END, string="0")
decimal_label = Label(text="Decimal Places")
decimal_places = Spinbox(from_=0, to=4, width=3, command=calculate)

# Positioning
miles_inp.grid(column=1, row=0)
miles_label.grid(column=2, row=0)
equal_label.grid(column=0, row=1)
conversion_label.grid(column=1, row=1)
km_label.grid(column=2, row=1)
calc_button.grid(column=1, row=2)
decimal_label.grid(column=0, row=3)
decimal_label.config(pady=15)
decimal_places.grid(column=1, row=3)

window.mainloop()
