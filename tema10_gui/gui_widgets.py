import sys
import tkinter
from tkinter import ttk

window = tkinter.Tk()

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

lista = ['Windows', 'macOS', 'MS DOS', 'AmigaOS', 'OS/2']
lista_items = tkinter.StringVar(value=lista)
listbox = tkinter.Listbox(window, height=10, listvariable=lista_items)

listbox.grid(column=0, row=0, sticky=tkinter.W, padx=50, pady=50)

selected = tkinter.StringVar()

r1 = ttk.Radiobutton(window, text='Si', value='1', variable=selected)
r2 = ttk.Radiobutton(window, text='No', value='2', variable=selected)
r3 = ttk.Radiobutton(window, text='Quizá', value='3', variable=selected)

r1.grid(column=0, row=1, padx=5, pady=5)
r2.grid(column=0, row=2, padx=5, pady=5)
r3.grid(column=0, row=3, padx=5, pady=5)

seleccionado2 = tkinter.StringVar()

rs1 = ttk.Radiobutton(window, text='SI2', value='4', variable=seleccionado2)
rs1.grid(column=0, row=4, padx=5, pady=5)




window.mainloop()
sys.exit(0)
