import tkinter

# Componentes y builders (botones, cajas, etiquetas...)

# Creando una ventanas
from textwrap import fill

window = tkinter.Tk()

# Metemos la geometrias. Hay que crear una serie de widgets
label_1 = tkinter.Label(window, text="label1", bg="orange", fg="white")
label_1.pack(ipadx=50, ipady=15)

label_2 = tkinter.Label(window, text="label2", bg="purple", fg="white")
label_2.pack(ipadx=50, ipady=15)

label_3 = tkinter.Label(window, text="label3", bg="blue", fg="white")
label_3.pack(ipadx=50, ipady=15)

label_4 = tkinter.Label(window, text="label4", bg="red", fg="white")
label_4.pack(ipadx=50, ipady=15, side='left', fill='x')

label_5 = tkinter.Label(window, text="label5", bg="yellow", fg="black")
label_5.pack(ipadx=50, ipady=15, side='left', fill='x')

label_6 = tkinter.Label(window, text="label6", bg="green", fg="white")
label_6.pack(ipadx=50, ipady=15, side='left', fill='x')

# Bucle que mantiene abierta una ventana
window.mainloop()
