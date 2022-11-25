from tkinter import *

v0 = Tk()
v1 = Toplevel(v0)

def mostrar(ventana): ventana.deicoinfy()
def ocultar(ventana): ventana.withdraw()
def ejecutar(f): v0.after(200,f)

b1 = Button(v0,text = "Terminar aplicación", command = v0.destroy).pack()
b2 = Button(v1,text = "Ocultar ventana", command = lambda:ejecutar(ocultar(v1))).pack()

v0.mainloop()