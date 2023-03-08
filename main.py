from tkinter import *

window = Tk()
window.title("Units Converter Program")

window.minsize(width=500, height=300)

label = Label(text="Enter miles here")
label.pack()

input = Entry()
input.pack()


def converter():
    kilometer = round(int(input.get()) * 1.609, 2)
    print(f"{kilometer}km")
    label.config(text=f"{kilometer}km")


button = Button(text="Convert", command=converter)
button.pack()

window.mainloop()


