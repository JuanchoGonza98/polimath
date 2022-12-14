import tkinter
from funciones_final2 import *
import tkinter as tk

#### VENTANA PARA CALCULAR LA SUMA ####
def InterfazSuma():
    Ventana.withdraw()
    Ventana1 = tk.Toplevel()
    Ventana1.geometry("400x390")
    Ventana1.config(bg="light green")
    Ventana1.title("Polimath.py")
    titulo = tkinter.Label(Ventana1, text="Suma de 2 polinomios.", bg="dark green", font="Broadway 20")
    titulo.pack(fill=tkinter.X)

    def Mostrar_grafico1():
        px = PX.get()
        pol1 = []
        ok = False
        if (len(px) >= 1 ):
            pol1 = leepol(px)
            ok = True
        else:
            ok = False
        if (ok == True and (len(pol1) <= 13 and len(pol1) >= 1)):
            graficapol(pol1)
        else:
            messagebox.showerror(message="Datos Ingresados incorrectos", title="ERROR")


    def Mostrar_grafico2():
        qx = QX.get()
        pol1 = []
        ok = False
        if (len(qx) >= 1):
            pol1 = leepol(qx)
            ok = True
        else:
            ok = False
        if (ok == True and (len(pol1) <= 13 and len(pol1) >= 1) ):
            graficapol(pol1)
        else:
            messagebox.showerror(message="Datos Ingresados incorrectos", title="ERROR")

    def mensaje():
        answer = messagebox.askyesno('Salir', "¿Desea Salir?...Confirme")
        if (answer):
            Ventana1.destroy()
            Ventana.deiconify()

  #Sustrae los datos de las cajas de texto y llama a las funciones a utilizar
    def CalcularSuma():
        polinomiop= PX.get()
        polinomioq=QX.get()
        px=[]
        qx=[]
        ok=False
        if (len(polinomioq)>=1 and len(polinomiop)>=1):
            px = leepol(polinomiop)
            qx = leepol(polinomioq)
            ok=True
        else:
            ok=False
        if(ok):
            flag1 = verifpol(px)
            while flag1 == 0:
                messagebox.showwarning('Invalido', "Verifique que el/los polinomios no sean de grado mayor a 12")
                polinomiop = PX.get()
                px = leepol(polinomiop)
                flag1 = verifpol(px)
            flag2 = verifpol(qx)
            while flag2 == 0:
                messagebox.showwarning('Invalido', "Verifique que el polinomio sea de grado menor a 13")
                polinomioq = QX.get()
                qx = leepol(polinomioq)
                flag2 = verifpol(qx)
        else:
            messagebox.showerror(message="Datos Ingresados incorrectos", title="ERROR")

        rx = []
        rx = sumapol(px, qx)
        cad = Representacion_poli(rx)
        Resultado.set(cad)


    PX = StringVar()
    QX = StringVar()
    Resultado = StringVar()

      #Elementos de la Interfaz
    cuadro_px=Entry(Ventana1, textvariable=PX, width=30)
    cuadro_px.place(x=100, y=70)
    text_px=Label(Ventana1, text="P(x)=", font="Elephant 16", bg="light green")
    text_px.place(x=20 ,y=70)

    cuadro_qx = Entry(Ventana1, textvariable=QX, width=30)
    cuadro_qx.place(x=100, y=130)
    text_px = Label(Ventana1, text="Q(x)=", font="Elephant 16", bg="light green")
    text_px.place(x=20, y=130)

    boton_Calcular = Button(Ventana1, text="Sumar", bg="green", font="Arial 11", command=CalcularSuma)
    boton_Calcular.place(x=160, y=180)

    txt_resultado=Label(Ventana1, text="El resultado es ", font="Elephant 14", bg="light green")
    txt_resultado.place(x=130, y=230)
    txt_rx=Label(Ventana1, text="R(x)=", font="Elephant 16", bg="light green")
    txt_rx.place(x=20, y=280)
    cuadro_resultado=Entry(Ventana1, textvariable=Resultado, width=30)
    cuadro_resultado.place(x=100, y=280)

    boton_Salir = Button(Ventana1, text="Salir", bg="green", font="Arial 10", command=mensaje)
    boton_Salir.place(x=300, y=340)
    boton_graf = Button(Ventana1, text="Gráfico P(x)", bg="green", font="Arial 9", command=Mostrar_grafico1)
    boton_graf.place(x=30, y=340)
    boton_graf2 = Button(Ventana1, text="Gráfico Q(x)", bg="green", font="Arial 9", command=Mostrar_grafico2)
    boton_graf2.place(x=120, y=340)

    Ventana1.mainloop()

####  VENTANA PARA CALCULAR LA MULTIPLICACIÓN####
def InterfazMutipli():          #Ventana de la funcion que multiplica dos polinomios
    Ventana.withdraw()
    Ventana2 = tk.Toplevel()
    Ventana2.geometry("410x390")
    Ventana2.config(bg="light green")
    Ventana2.title("Polimath.py")
    titulo = tkinter.Label(Ventana2, text="Multiplicación de 2 polinomios.", bg="dark green", font="Broadway 16")
    titulo.pack(fill=tkinter.X)

    def Mostrar_grafico1():
        px = Px.get()
        pol1 = []
        ok = False
        if (len(px) >= 1 ):
            pol1 = leepol(px)
            ok = True
        else:
            ok = False
        if (ok == True and (len(pol1) <= 13 and len(pol1) >= 1)):
            graficapol(pol1)
        else:
            messagebox.showerror(message="Datos Ingresados incorrectos", title="ERROR")


    def Mostrar_grafico2():
        qx = QX.get()
        pol1 = []
        ok = False
        if (len(qx) >= 1):
            pol1 = leepol(qx)
            ok = True
        else:
            ok = False
        if (ok == True and (len(pol1) <= 13 and len(pol1) >= 1) ):
            graficapol(pol1)
        else:
            messagebox.showerror(message="Datos Ingresados incorrectos", title="ERROR")

  #Mensaje para alertar de la salida
    def mensaje():
        answer = messagebox.askyesno('Salir', "¿Desea Salir?...Confirme")
        if (answer):
            Ventana2.destroy()
            Ventana.deiconify()


    #Metodo que sustrae los datos introducidos y realiza llamadas a las funciones a utilizar
    def CalcularMulti():
        polinomiop = Px.get()
        polinomioq = QX.get()
        px = []
        qx = []
        ok = False
        if (len(polinomioq) >= 1 and len(polinomiop) >= 1):
            px = leepol(polinomiop)
            qx = leepol(polinomioq)
            ok = True
        else:
            ok = False
        if (ok):
            flag1 = verifpol(px)
            while flag1 == 0:
                messagebox.showwarning('Invalido', "Verifique que el/los polinomios no sean de grado mayor a 12")
                polinomiop = Px.get()
                px = leepol(polinomiop)
                flag1 = verifpol(px)
            flag2 = verifpol(qx)
            while flag2 == 0:
                messagebox.showwarning('Invalido', "Verifique que el polinomio sea de grado menor a 13")
                polinomioq = QX.get()
                qx = leepol(polinomioq)
                flag2 = verifpol(qx)
        else:
            messagebox.showerror(message="Datos Ingresados incorrectos", title="ERROR")

        Resultado.set(multpol(px, qx))


    Px = StringVar()
    QX = StringVar()
    Resultado = StringVar()


    Px=StringVar()
    QX=StringVar()
    Resultado=StringVar()

      #Elementos de la interfaz
    cuadro_px=Entry(Ventana2, textvariable=Px, width=30)
    cuadro_px.place(x=100, y=70)
    text_px=Label(Ventana2, text="P(x)=", font="Elephant 16", bg="light green")
    text_px.place(x=20 ,y=70)
    cuadro_qx = Entry(Ventana2, textvariable=QX, width=30)
    cuadro_qx.place(x=100, y=130)
    text_px = Label(Ventana2, text="Q(x)=", font="Elephant 16", bg="light green")
    text_px.place(x=20, y=130)
    boton_Calcular = Button(Ventana2, text="Multiplicar", bg="green", font="Arial 11", command=CalcularMulti)
    boton_Calcular.place(x=160, y=180)
    txt_resultado=Label(Ventana2, text="El resultado es ", font="Elephant 14", bg="light green")
    txt_resultado.place(x=130, y=230)
    txt_rx=Label(Ventana2, text="R(x)=", font="Elephant 16", bg="light green")
    txt_rx.place(x=20, y=280)
    cuadro_resultado=Entry(Ventana2, textvariable=Resultado, width=30)
    cuadro_resultado.place(x=100, y=280)

    boton_Salir = Button(Ventana2, text="Salir", bg="green", font="Arial 10", command=mensaje)
    boton_Salir.place(x=300, y=340)
    boton_graf = Button(Ventana2, text="Gráfico P(x)", bg="green", font="Arial 9", command=Mostrar_grafico1)
    boton_graf.place(x=30, y=340)
    boton_graf2 = Button(Ventana2, text="Gráfico Q(x)", bg="green", font="Arial 9", command=Mostrar_grafico2)
    boton_graf2.place(x=120, y=340)


    Ventana2.mainloop()

####VENTANA PARA CALCULAR LAS RAICES DE UN POLINIMIO####
def InterfazRaices():
    Ventana.withdraw()
    Ventana3 = tk.Toplevel()
    Ventana3.geometry("400x390")
    Ventana3.config(bg="light green")
    Ventana3.title("Polimath.py")
    titulo = tkinter.Label(Ventana3, text="Raíces de P(x).", bg="dark green", font="Broadway 20")
    titulo.pack(fill=tkinter.X)
    def Mostrar_grafico():
        px=Px.get()
        pol1=[]
        ok=False
        if (len(px)>=1):
            pol1=leepol(px)
            ok=True
        else:
            ok=False
        if (ok==True and (len(pol1)<=13 and len(pol1)>=1) ):
            graficapol(pol1)
        else:
            messagebox.showerror(message="Datos Ingresados incorrectos", title="ERROR")


    def mensaje():
        answer = messagebox.askyesno('Salir', "¿Desea Salir?...Confirme")
        if (answer):
            Ventana3.destroy()
            Ventana.deiconify()

    def CalcularRaiz():
        polinomio=Px.get()
        lim_inf=X1.get()
        lim_sup=X2.get()
        px=[]
        resul=[]
        aux=[]
        if (es_entero(lim_inf) and es_entero(lim_sup)  and len(polinomio)>=1 ): #Verificación de que los datos ingresados sean correctos
            px=leepol(polinomio)
            x1 = int(lim_inf)
            x2 = int(lim_sup)
            ok=True
        else:
            ok=False
        if (ok):
            flag1 = verifpol(px)
            while flag1 == 0:
                messagebox.showwarning('Invalido', "Verifique que el  polinomio no sea de grado mayor a 12")
                polinomio = Px.get()
                px = leepol(polinomio)
                flag1 = verifpol(px)
            resul = raicespol(px, x1, x2) #llamada a la función raicespol
            for i in range(len(resul)):
                cadena = "x= " + str(resul[i])
                aux.append(cadena)
            salida = " ".join(aux)
            if(len(resul)==0):
                salida="No posee raices reales en en rango ingresado"
            Resul.set(salida)
        else:
            messagebox.showerror(message="Datos Ingresados incorrectos", title="ERROR")

    Px = StringVar()
    X1 = StringVar()
    X2 = StringVar()
    Resul= StringVar()

    cuadro_px = Entry(Ventana3, textvariable=Px, width=30)
    cuadro_px.place(x=140, y=70)
    text_px = Label(Ventana3, text="P(x)=", font="Elephant 16", bg="light green")
    text_px.place(x=50, y=65)

    cuadro_x1 = Entry(Ventana3, textvariable=X1, width=15)
    cuadro_x1.place(x=60, y=160)
    text_x1 = Label(Ventana3, text="X1", font="Elephant 16", bg="light green")
    text_x1.place(x=90, y=120)

    cuadro_x2 = Entry(Ventana3, textvariable=X2, width=15)
    cuadro_x2.place(x=250, y=160)
    text_x2 = Label(Ventana3, text="X2", font="Elephant 16", bg="light green")
    text_x2.place(x=280, y=120)

    cuadro_resultado=Entry(Ventana3, textvariable=Resul, width=30)
    cuadro_resultado.place(x=120, y=280)
    text_Resul=Label(Ventana3, text="Las Raices Son X= ", font="Elephant 12", bg="light green")
    text_Resul.place(x=140, y=250)

    boton_Calcular = Button(Ventana3, text="Calcular", bg="green", font="Arial 11", command=CalcularRaiz)
    boton_Calcular.place(x=170, y=200)

    boton_Salir = Button(Ventana3, text="Salir", bg="green", font="Arial 10", command=mensaje)
    boton_Salir.place(x=300, y=330)
    boton_graf = Button(Ventana3, text="Mostrar Gráfico", bg="green", font="Arial 9", command=Mostrar_grafico)
    boton_graf.place(x=30, y=330)

    Ventana3.mainloop()

####VENTANA PARA CALCULAR EL MINIMO Y EL MAXIMO DE UNA FUNCIÓN####
def InterfazMaxM():
    Ventana.withdraw()
    Ventana4 = tk.Toplevel()
    Ventana4.geometry("400x390")
    Ventana4.config(bg="light green")
    Ventana4.title("Polimath.py")
    titulo = tkinter.Label(Ventana4, text="Máximo y Mínimo de P(x) entre x1 y x2.", bg="dark green", font="Broadway 12")
    titulo.pack(fill=tkinter.X)
    def Mostrar_grafico():
        px=Px.get()
        pol1=[]
        ok=False
        if (len(px)>=1 ):
            pol1=leepol(px)
            ok=True
        else:
            ok=False
        if (ok==True and (len(pol1)<=13 and len(pol1)>=1) ):
            graficapol(pol1)
        else:
            messagebox.showerror(message="Datos Ingresados incorrectos", title="ERROR")


    def mensaje():
        answer = messagebox.askyesno('Salir', "¿Desea Salir?...Confirme")
        if (answer):
            Ventana4.destroy()
            Ventana.deiconify()

    def Calcularmm():
        polinomio=Px.get()
        lim_inf=X1.get()
        lim_sup=X2.get()
        px=[]
        ok=False
        if (es_entero(lim_inf) and es_entero(lim_sup) and len(polinomio) >= 1):  # Verificación de que los datos ingresados sean correctos
            px = leepol(polinomio)
            x1 = int(lim_inf)
            x2 = int(lim_sup)
            ok = True
        else:
            ok = False
        if (ok):
            flag1 = verifpol(px)
            while flag1 == 0:
                messagebox.showwarning('Invalido', "Verifique que el  polinomio no sea de grado mayor a 12")
                polinomio = Px.get()
                px = leepol(polinomio)
                flag1 = verifpol(px)
            maximo, xmax, minimo, xmin = maxminpol(px, x1, x2)
            Max.set(maximo)
            XMAX.set(xmax)
            Min.set(minimo)
            XMIN.set(xmin)
        else:
            messagebox.showerror(message="Datos Ingresados incorrectos", title="ERROR")

    Px = StringVar()
    X1 = StringVar()
    X2 = StringVar()
    Max=StringVar()
    Min= StringVar()
    XMAX=StringVar()
    XMIN= StringVar()

    cuadro_px = Entry(Ventana4, textvariable=Px, width=30)
    cuadro_px.place(x=140, y=70)
    text_px = Label(Ventana4, text="P(x)=", font="Elephant 16", bg="light green")
    text_px.place(x=50, y=65)

    cuadro_x1 = Entry(Ventana4, textvariable=X1, width=15)
    cuadro_x1.place(x=60, y=160)
    text_x1 = Label(Ventana4, text="X1", font="Elephant 16", bg="light green")
    text_x1.place(x=90, y=120)

    cuadro_x2 = Entry(Ventana4, textvariable=X2, width=15)
    cuadro_x2.place(x=250, y=160)
    text_x2 = Label(Ventana4, text="X2", font="Elephant 16", bg="light green")
    text_x2.place(x=280, y=120)

    #Salida del valor máximo de la función
    cuadro_Max=Entry(Ventana4, textvariable=Max, width=15)
    cuadro_Max.place(x=55, y=250)
    textMax=Label(Ventana4, text="Máximo", font= "Elephant 14", bg="light green")
    textMax.place(x=60, y=220)
    cuadro_Xmax=Entry(Ventana4, textvariable=XMAX, width=10)
    cuadro_Xmax.place(x=60, y=320)
    text_xmax=Label(Ventana4, text="Con x=", font="Elephant 14 ", bg="light green")
    text_xmax.place(x=50, y=290 )

    boton_Calcular = Button(Ventana4, text="Calcular", bg="green", font="Arial 11", command=Calcularmm)
    boton_Calcular.place(x=170, y=200)

    #Salida del valor minimo de la función
    cuadro_Min=Entry(Ventana4, textvariable=Min, width=15)
    cuadro_Min.place(x=260, y=260)
    text_min=Label(Ventana4, text="Mínimo", font="Elephant 14", bg="light green")
    text_min.place(x=270, y=220)
    cuadroxmin = Entry(Ventana4, textvariable=XMIN, width=10)
    cuadroxmin.place(x=270, y=320)
    text_xmin = Label(Ventana4, text="Con x=", font="Elephant 14", bg="light green")
    text_xmin.place(x=270, y=290)

    boton_Salir = Button(Ventana4, text="Salir", bg="green", font="Arial 10", command=mensaje)
    boton_Salir.place(x=320, y=350)
    boton_graf = Button(Ventana4, text="Mostrar Gráfico", bg="green", font="Arial 9", command=Mostrar_grafico)
    boton_graf.place(x=30, y=350)

    Ventana4.mainloop()

####VENTANA PARA CALCULRA LA DERIVADA DE UN POLINOMIO####
def InterfazDerivada():
  Ventana.withdraw()
  Ventana4 = tk.Toplevel()
  Ventana4.geometry("400x390")
  Ventana4.config(bg="light green")
  Ventana4.title("Polimath.py")
  titulo = tkinter.Label(Ventana4, text="Derivada de P(x).", bg="dark green", font="Broadway 20")
  titulo.pack(fill=tkinter.X)

  def Mostrar_grafico():
      px = Px.get()
      pol1 = []
      ok = False
      if (len(px) >= 1 ):
          pol1 = leepol(px)
          ok = True
      else:
          ok=False
      if (ok == True and (len(pol1) <= 13 and len(pol1) >= 1)):
          graficapol(pol1)
      else:
          messagebox.showerror(message="Datos Ingresados incorrectos", title="ERROR")

  def mensaje():
        answer = messagebox.askyesno('Salir', "¿Desea Salir?...Confirme")
        if (answer):
            Ventana4.destroy()
            Ventana.deiconify()

  #sustrae los elementos de las cajas de texto y realiza las llamadas a las funciones requeridas
  def CalcularDerivada():
    polinomiop=Px.get()
    px=[]
    rx=[]
    ok = False
    if ( len(polinomiop) >= 1):  # Verificación de que los datos ingresados sean correctos
        px = leepol(polinomiop)
        ok = True
    else:
        ok = False
    if (ok):
        flag1 = verifpol(px)
        while flag1 == 0:
            messagebox.showwarning('Invalido', "Verifique que el  polinomio no sea de grado mayor a 12")
            polinomiop = Px.get()
            px = leepol(polinomiop)
            flag1 = verifpol(px)
        rx = derivapol(px)
        cad = Representacion_poli(rx)
        Resultado.set(cad)
    else:
        messagebox.showerror(message="Datos Ingresados incorrectos", title="ERROR")


  Px=StringVar()
  QX=StringVar()
  Resultado=StringVar()

  #Elementos de la interfaz gráfica

  cuadro_px=Entry(Ventana4, textvariable=Px, width=30)
  cuadro_px.place(x=130, y=100)
  text_px=Label(Ventana4, text="P(x)=", font="Elephant 16", bg="light green")
  text_px.place(x=30 ,y=95)

  boton_Calcular = Button(Ventana4, text="Derivar", bg="green", font="Arial 11", command=CalcularDerivada)
  boton_Calcular.place(x=160, y=160)

  txt_resultado=Label(Ventana4, text="Su derivada es: ", font="Elephant 14", bg="light green")
  txt_resultado.place(x=130, y=220)
  txt_rx=Label(Ventana4, text="P'(x)=", font="Elephant 16", bg="light green")
  txt_rx.place(x=30, y=255)
  cuadro_resultado=Entry(Ventana4, textvariable=Resultado, width=30)
  cuadro_resultado.place(x=130, y=260)

  boton_Salir = Button(Ventana4, text="Salir", bg="green", font="Arial 10", command=mensaje)
  boton_Salir.place(x=300, y=320)
  boton_graf = Button(Ventana4, text="Gráfico P(x)", bg="green", font="Arial 9", command=Mostrar_grafico)
  boton_graf.place(x=30, y=320)


  Ventana4.mainloop()

###VENTANA PARA CALCULAR LA INTEGRAL DEFINIDA ENTRE X1 Y X2####
def InterfazIntegral():
    Ventana.withdraw()
    Ventana5 = tk.Toplevel()
    Ventana5.geometry("400x350")
    Ventana5.config(bg="light green")
    Ventana5.title("Polimath.py")
    titulo = tkinter.Label(Ventana5, text="Integral definida de P(x).", bg="dark green")
    titulo.pack(fill=tkinter.X)
    fondo=PhotoImage(file="fondointegral.gif")
    LabFondo=Label(Ventana5, image=fondo).place(x=0, y=0)

    def Mostrar_grafico():
        px=Px.get()
        pol1=[]
        ok=False
        if (len(px)>=1 ):
            pol1=leepol(px)
            ok=True
        else:
            ok=False
        if (ok and (len(pol1)<=13 and len(pol1)>=1) ):
            graficapol(pol1)
        else:
            messagebox.showerror(message="Datos Ingresados incorrectos", title="ERROR")


    def mensaje():
        answer = messagebox.askyesno('Salir', "¿Desea Salir?...Confirme")
        if (answer):
            Ventana5.destroy()
            Ventana.deiconify()

    #Metodo que extrae los datos de entrada y realiza la llamado a las funciones requeridas
    def Ent_Sal():
        entrada=Px.get()
        lim_inf=X1.get()
        lim_sup=X2.get()
        ok=False
        px=[]
        if (es_entero(lim_inf) and es_entero(lim_sup) and len(entrada) >= 1):  # Verificación de que los datos ingresados sean correctos
            px = leepol(entrada)
            x1 = int(lim_inf)
            x2 = int(lim_sup)
            ok = True
        else:
            ok = False
        if (ok):
            flag1 = verifpol(px)
            while flag1 == 0:
                messagebox.showwarning('Invalido', "Verifique que el  polinomio no sea de grado mayor a 12")
                entrada = Px.get()
                px = leepol(entrada)
                flag1 = verifpol(px)

            inte = integrapol(px, x1, x2)
            Resultado.set(inte)
        else:
            messagebox.showerror(message="Datos Ingresados incorrectos", title="ERROR")

    #Elementos de la interfaz gráfica
    Px = StringVar()
    X1 = StringVar()
    X2 = StringVar()
    Resultado = StringVar()

    #entradas
    Titulo=Label(Ventana5, text=" Integral definida de P(x) ", font="Broadway 22", bg="dark green")
    Titulo.place(x=0, y=0)
    cuadro_x2 = Entry(Ventana5, textvariable=X2, width=10)
    cuadro_x2.place(x=190, y=55)
    cuadro_px = Entry(Ventana5, textvariable=Px, width=30)
    cuadro_px.place(x=140, y=130)
    cuadro_x1 = Entry(Ventana5, textvariable=X1, width=10)
    cuadro_x1.place(x=135, y=200)

    cuadro_sal=Entry(Ventana5, textvariable=Resultado)
    cuadro_sal.place(x=140, y=280)
    #botones
    boton_Calcular = Button(Ventana5, text="Calcular", bg="green", font="Arial 11", command=Ent_Sal)
    boton_Calcular.place(x=160, y=235)
    boton_salir = Button(Ventana5, text="Salir", bg="green", font="Arial 10", command=mensaje)
    boton_salir.place(x=330, y=300)
    boton_graf=Button(Ventana5, text="Mostrar Gráfico", bg="green", font="Arial 9", command=Mostrar_grafico)
    boton_graf.place(x=30, y=300)

    Ventana5.mainloop()


####VENTANA PARA GRAFICAR UN POLINOMIO####
def InterfazGrafico():
    Ventana.withdraw()
    Ventana7 = tk.Toplevel()
    Ventana7.geometry("400x300")
    Ventana7.config(bg="light green")
    Ventana7.title("Polimath.py")
    titulo = tkinter.Label(Ventana7, text="Gráfica de P(x).", bg="dark green", font="Broadway 20")
    titulo.pack(fill=tkinter.X)

    def mensaje():
        answer = messagebox.askyesno('Salir', "¿Desea Salir?...Confirme")
        if (answer):
            Ventana7.destroy()
            Ventana.deiconify()

    def Graficar():
        polinomio=Px.get()
        lim_inf=(X1.get())
        lim_sup=(X2.get())
        px=[]
        if (es_entero(lim_inf) and es_entero(lim_sup) and len(polinomio) >= 1):  # Verificación de que los datos ingresados sean correctos
            px = leepol(polinomio)
            x1 = int(lim_inf)
            x2 = int(lim_sup)
            ok = True
        else:
            ok = False
        if (ok):
            flag1 = verifpol(px)
            while flag1 == 0:
                messagebox.showwarning('Invalido', "Verifique que el  polinomio no sea de grado mayor a 12")
                polinomio = Px.get()
                px = leepol(polinomio)
                flag1 = verifpol(px)
            graficapol(px)
        else:
            messagebox.showerror(message="Datos Ingresados incorrectos", title="ERROR")




    Px=StringVar()
    X1=StringVar()
    X2=StringVar()

    cuadro_px = Entry(Ventana7, textvariable=Px, width=30)
    cuadro_px.place(x=140, y=70)
    text_px = Label(Ventana7, text="P(x)=", font="Elephant 16", bg="light green")
    text_px.place(x=50, y=65)

    cuadro_x1=Entry(Ventana7, textvariable=X1, width=15)
    cuadro_x1.place(x=60, y=160)
    text_x1=Label(Ventana7, text="X1", font="Elephant 16", bg="light green")
    text_x1.place(x=90, y=120)

    cuadro_x2 = Entry(Ventana7, textvariable=X2, width=15)
    cuadro_x2.place(x=250, y=160)
    text_x2 = Label(Ventana7, text="X2", font="Elephant 16", bg="light green")
    text_x2.place(x=280, y=120)

    boton_Calcular = Button(Ventana7, text="Graficar", bg="green", font="Arial 11", command=Graficar)
    boton_Calcular.place(x=170, y=200)

    boton_Salir = Button(Ventana7, text="Salir", bg="green", font="Arial 10", command=mensaje)
    boton_Salir.place(x=290, y=220)

    Ventana7.mainloop()

####VENTANA EMERGENTE PARA ADEVERTIR DE LA SALIDA####
def mensaje():
    answer = messagebox.askyesno('Salir', "¿Desea Salir?...Confirme")
    if (answer):
        Ventana.destroy()


######VENTANA DEL MENÚ PRINCIPAL######
Ventana = tkinter.Tk()
Ventana.geometry("800x600")
Ventana.config(bg="green")
Ventana.title("Grupo 4")
cabezera = tkinter.Label(Ventana, text="Polimath.py", bg="orange", font="Broadway 40")
cabezera.pack(fill=tkinter.X)
photo1 = PhotoImage(file="polim.gif")
imgBoton4 = PhotoImage(file="derivada.gif")
imgBoton5= PhotoImage(file="integral.gif")
imgBoton6= PhotoImage(file="min.gif")



########Elemetos de la interfaz########
i2 = Label(Ventana, image=photo1).place(x=300, y=95)
###Botones que llaman a las funciones para realizar las operaciones con los polinomios####
btnSuma=Button(Ventana,text = "P(x)+Q(x)" , font="Elephant 18", bg="dark orange", command=InterfazSuma)  .place(x=50, y=330)
btnPro=Button(Ventana,text = "P(x)*Q(x)" , font="Elephant 18", bg= "dark orange", command=InterfazMutipli).place(x=270, y=330)
btnRaiz=Button(Ventana, text = "P(x)=0" , font="Elephant 18", bg="dark orange", command=InterfazRaices).place(x=480, y=330)
btnDerivada = Button(Ventana, image=imgBoton4, height=50, width=100, bg="dark orange", command=InterfazDerivada).place(x=650, y=330)
btnIntegral = Button(Ventana, image=imgBoton5, height=50, width=100, bg= "dark orange", command=InterfazIntegral).place(x=80, y=450)
btnMinMax= Button(Ventana, image=imgBoton6, height=50, width=100, bg="dark orange", command=InterfazMaxM).place(x=290, y=450)
btnGrafico= Button(Ventana, text="Gráfico", font="Elephant 18", bg="dark orange", command=InterfazGrafico).place(x=485, y=450)
btnExit = Button(Ventana, text="Salir", font="Elephant 18", bg="light blue", command=mensaje).place(x=660, y=450)




Ventana.mainloop()

