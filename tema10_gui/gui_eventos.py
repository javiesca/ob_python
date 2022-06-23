import tkinter

window = tkinter.Tk()

def saludar(event):
    print("Han hecho click en saludar")

def saludarDoubleClick(event):
    print("Han hecho DOBLE click en el boton saludar")

def salir(event):
    print("Adiooooos")
    window.quit()


boton = tkinter.Button(window, text='Haz click para Saludar')
boton.pack()

#EVENTOS
boton.bind('<Button-1>',saludar)
boton.bind('<Double-1>',saludarDoubleClick)

botonSalir = tkinter.Button(window, text='Haz click para Salir')
botonSalir.pack()

#EVENTOS
botonSalir.bind('<Button-1>',salir)
botonSalir.bind('<Double-1>',saludarDoubleClick)


window.mainloop()