from tkinter import *

window = Tk()
window.title("Units Converter Program")

window.minsize(width=500, height=300)

label = Label(text="Enter miles here")
label.grid(column=0, row=0)

input = Entry(width=10)
input.grid(column=3, row=2)


def converter():
    kilometer = round(int(input.get()) * 1.609, 2)
    print(f"{kilometer}km")
    label.config(text=f"{kilometer}km")


button = Button(text="Convert", command=converter)
button.grid(column=1, row=1)

new_botton = Button(text="New Button")
new_botton.grid(column=2, row=0)

window.mainloop()


