import tkinter as tk
from tkinter import messagebox
def color_amarillo():
    ventana['bg'] = 'yellow'
def color_verde():
    ventana['bg'] = 'green'
def color_cafe():
    ventana['bg'] = 'brown'

def color_rojo():
    ventana['bg'] = 'red'

def color_gris():
    ventana['bg'] = 'grey'

def mensaje():
    answer=messagebox.askyesno('Salir', "¿Desea Salir?...Confirme")
    if(answer):
        ventana.destroy()

ventana = tk.Tk() #Se crea la ventana principal que contendra a todas las demas
ventana.title("Polimath V1.01") #Titulo de la ventana
ventana.geometry("600x300") #Se define un tamaño generico para la ventana

mi_menu = tk.Menu(ventana) #Se declara la variable mi_menu que estara dentro de la ventana principal
mi_menu.add_command(label='Amarillo', command=color_amarillo)
mi_menu.add_command(label='Verde', command=color_verde)
mi_menu.add_command(label='Cafe',command=color_cafe)

mi_dropdown_menu= tk.Menu(mi_menu)
mi_dropdown_menu=tk.Menu(mi_menu, tearoff=0)
mi_dropdown_menu.add_command(label='Rojo', command=color_rojo)
mi_dropdown_menu.add_command(label='Gris', command=color_gris)

mi_menu.add_command(label='Salir', command=mensaje)

mi_menu.add_cascade(label='Otros colores',menu=mi_dropdown_menu)
ventana.config(menu=mi_menu)
ventana.mainloop()
