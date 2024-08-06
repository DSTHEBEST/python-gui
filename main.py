"""def add(*args):
    summ = 0
    for n in args:
        summ += n
    print(summ)


add(2, 6, 7, 8, 9)"""
from tkinter import *

window = Tk()
window.title("Wassup my g")
window.minsize(width=500, height=300)

my_label = Label(text="IM a Label")
my_label.pack(side="top")

my_label.config(text="new name bro")


def button_click():
    new_text = inputt.get()
    my_label.config(text=new_text)


button = Button(text="Click me", command=button_click)
button.pack()

inputt = Entry(width=10)
inputt.pack()
print(inputt.get())

window.mainloop()
