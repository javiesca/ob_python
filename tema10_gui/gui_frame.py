import random
import tkinter
from tkinter import ttk

window = tkinter.Tk()

colors = ['blue', 'green', 'red', 'yellow','black']

for x in range(0,10):
    color = random.randint(0, len(colors))
    color2 = random.randint(0, len(colors))

label1 = tkinter.Label(window, text="Posicionamiento absoluto", bg='blue', fg="white")
label1.place(x=10, y=50)

label1 = tkinter.Label(window, text="Otro texto", bg='red', fg="white")
label1.place(x=25, y=30)

window.mainloop()