from tkinter import *

window = Tk()
window.minsize(width=500, height=300)
window.title("Mile to Km Converter")
window.config(pady=100, padx=150)

miles_input = Entry()
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

km_value = Label(text="0")
km_value.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)


def convert():
    conversion = round(int(miles_input.get()) * 1.609, 2)
    km_value.config(text=f"{conversion}")


button = Button(text="Calculate", command=convert)
button.grid(column=1, row=2)


window.mainloop()

