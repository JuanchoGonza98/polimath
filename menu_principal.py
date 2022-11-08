import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
def Principal():
    def mensaje():
        answer = messagebox.askyesno('Salir', "¿Desea Salir?...Confirme")
        if (answer):
            Ventana.destroy()
    def submenu_suma():
        #Se crea ventana secundaria
        ventana_secundaria = tkinter.Toplevel()
        ventana_secundaria.title("Suma de polinomios Q(x) + P(x) ")
        ventana_secundaria.config(width=550, height=720)
        boton_cerrar = tkinter.Button(
            ventana_secundaria,
            text="Cerrar ventana",
            command=ventana_secundaria.destroy
        )
        boton_cerrar.place(x=75, y=75)
    Ventana = tkinter.Tk()
    Ventana.geometry("800x600")
    Ventana.config(bg="green")
    Ventana.title("Grupo 7")
    cabezera = tkinter.Label(Ventana, text="Polimath.py", bg="orange", font="Broadway 40")
    cabezera.pack(fill=tkinter.X)
    photo1 = PhotoImage(file="polim.gif")
    imgBoton4 = PhotoImage(file="derivada.gif")
    imgBoton5= PhotoImage(file="integral.gif")
    imgBoton6= PhotoImage(file="min.gif")

    i2 = Label(Ventana, image=photo1).place(x=300, y=95)
    btnSuma=Button(Ventana,text = "P(x)+Q(x)" , font="Elephant 18", bg="dark orange",command=submenu_suma)  .place(x=50, y=330)
    btnPro=Button(Ventana,text = "P(x)*Q(x)" , font="Elephant 18", bg= "dark orange").place(x=270, y=330)
    btnRaiz=Button(Ventana, text = "P(x)=0" , font="Elephant 18", bg="dark orange").place(x=480, y=330)
    btnDerivada = Button(Ventana, image=imgBoton4, height=50, width=100, bg="dark orange").place(x=650, y=330)
    btnIntegral = Button(Ventana, image=imgBoton5, height=50, width=100, bg= "dark orange").place(x=80, y=450)
    btnMinMax= Button(Ventana, image=imgBoton6, height=50, width=100, bg="dark orange").place(x=290, y=450)
    btnGrafico= Button(Ventana, text="Gráfico", font="Elephant 18", bg="dark orange").place(x=485, y=450)
    btnExit = Button(Ventana, text="Salir", font="Elephant 18", bg="light blue",command=mensaje).place(x=660, y=450)
    Ventana.mainloop()


Principal()
