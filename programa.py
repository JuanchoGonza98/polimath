import tkinter
from tkinter import *


def Principal():
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
    btnSuma=Button(Ventana,text = "P(x)+Q(x)" , font="Elephant 18", bg="dark orange")  .place(x=50, y=330)
    btnPro=Button(Ventana,text = "P(x)*Q(x)" , font="Elephant 18", bg= "dark orange").place(x=270, y=330)
    btnRaiz=Button(Ventana, text = "P(x)=0" , font="Elephant 18", bg="dark orange").place(x=480, y=330)
    btnDerivada = Button(Ventana, image=imgBoton4, height=50, width=100, bg="dark orange").place(x=650, y=330)
    btnIntegral = Button(Ventana, image=imgBoton5, height=50, width=100, bg= "dark orange").place(x=80, y=450)
    btnMinMax= Button(Ventana, image=imgBoton6, height=50, width=100, bg="dark orange").place(x=290, y=450)
    btnGrafico= Button(Ventana, text="Gráfico", font="Elephant 18", bg="dark orange").place(x=485, y=450)
    btnExit = Button(Ventana, text="Salir", font="Elephant 18", bg="light blue").place(x=660, y=450)
    Ventana.mainloop()


Principal()
