#Librerias a utilizar
import tkinter
from tkinter import *
import re
from tkinter import messagebox
from tkinter import ttk
import matplotlib.pyplot as plt
import re

#########FUNCIONES PRINCIPALES#########
#función que recibe una cadena que contine el polinomio y que retorna una lista de coeficientes del polimonio con sus respecitivos grados

def leepol(entrada):
  regexp = r"([+-]?)(?:\s*)(\d*)(x?)(?:\^)?(\d+)?"
  c = {}
  for sign, coef, x, exp in re.findall(regexp, entrada):
    # print(f"{sign}, {coef}, {x}, {exp}")
    if not coef and not x:
      continue

    if x and not coef:
      coef = '1'
    if x and sign == "-":
      coef = "-" + coef
    if not x and sign == "-":
      coef='-'+coef
    if x and not exp:
      exp = '1'
    if coef and not x :
      exp = '0'


    exp = int(exp)
    c[exp] = int(coef)

  grado = max(c)
  coeficientes = [0.0] * (grado+1)
  for g, v in c.items():
    coeficientes[g] = v

  return coeficientes






def Representacion_poli(entrada):  # recibe la lista donde se encuentra el polinomio
  longitud = len(entrada) - 1  # variable aux para recorrer la lista entrada
  n = longitud
  aux = []  # lista para guardar cada monomio

  if (len(entrada) == 1):
    aux.append(str(entrada[0]))
  else:
    for i in range(len(entrada)):
      if (longitud == n and entrada[longitud] != 0):  # evitar el caracter de concatenación + al primer elemento
        if (longitud > 1):
          # Verificacion del coeficiente 1
          if (entrada[longitud] == -1):
            elemento = '-' + 'x^' + str(longitud)
            aux.append(elemento)
          elif (entrada[longitud] != 1 and entrada[longitud] != -1):
            elemento = str(entrada[longitud]) + 'x^' + str(longitud)
            aux.append(elemento)
          else:
            elemento = 'x^' + str(longitud)
            aux.append(elemento)

        else:
          if (entrada[longitud] == -1):  # Verificacion para coeficientes -1
            elemento = '-' + 'x^' + str(longitud)
            aux.append(elemento)

          elif (entrada[longitud] != 1 and entrada[longitud] != -1):
            elemento = str(entrada[longitud]) + 'x'
            aux.append(elemento)
          else:
            elemento = 'x'
            aux.append(elemento)

      if (longitud != n and longitud > 1 and entrada[
        longitud] != 0):  # si es el primer elemeto añadir caracter + en caso de los positivos
        if (entrada[longitud] < 0):
          if (entrada[longitud] != -1):
            elemento = str(entrada[longitud]) + 'x^' + str(longitud)
            aux.append(elemento)
          else:
            elemento = '-' + 'x^' + str(longitud)
            aux.append(elemento)
        else:
          if (entrada[longitud] != 1):
            elemento = '+' + str(entrada[longitud]) + 'x^' + str(longitud)
            aux.append(elemento)
          else:
            elemento = '+' + 'x^' + str(longitud)
            aux.append(elemento)

      if (longitud == 1 and entrada[longitud] != 0 and longitud != n):  # evitar el caracter ^ cuando el exponente es 1
        if (entrada[longitud] < 0):
          if (entrada[longitud] != -1):
            elemento = str(entrada[longitud]) + 'x'
            aux.append(elemento)
          else:
            elemento = '- ' + 'x'
            aux.append(elemento)
        else:
          if (entrada[longitud] != 1):
            elemento = '+' + str(entrada[longitud]) + 'x'
            aux.append(elemento)
          else:
            elemento = '+ ' + 'x'
            aux.append(elemento)

      if (longitud == 0 and entrada[longitud] != 0):  # evitar la variable x para el termino independiente
        if (entrada[longitud] < 0):
          elemento = str(entrada[longitud])
          aux.append(elemento)
        else:
          elemento = '+' + str(entrada[longitud])
          aux.append(elemento)
      longitud = longitud - 1
  cad = "".join(aux)  # covertir la lista de monomios en una sola cadena  y retornar la cadena
  return cad


###############FUNCIONES DE CADA OPERACIÓN###############
def sumapol(P,Q):
  aux = 0
  if len(P) > len(Q):
    mayor = len(P)
    menor = len(Q)
    sum = [0]*mayor
    for i in range(menor):
      sum[i] = P[i] + Q[i]
      aux = aux + 1
    while aux < mayor:
      sum[aux] = P[aux]
      aux = aux + 1
  elif len(P) == len(Q):
    mayor = len(P)
    sum = [0]*mayor
    for i in range(mayor):
      sum[i] = P[i] + Q[i]
  else:
    mayor = len(Q)
    menor = len(P)
    sum = [0]*mayor
    for i in range(menor):
      sum[i] = P[i] + Q[i]
      aux = aux + 1
    while aux < mayor:
      sum[aux] = Q[aux]
      aux = aux + 1
  return sum
#####FUNCION DERIVAPOL######
def derivapol(F):
    for j in range(len(F)):
        F[j] = j * F[j]
    der = [0] * (len(F) - 1)
    for i in range(len(F)-1):
        der[i] = F[i+1]
    return der
#funcion que recibe 2 listas y retorna otra lista que contiene la multiplicación de las listas recibidas
def mulpol(pol1,pol2):
  auxcoef = [0] * (len(pol1)*len(pol2))
  auxexp = [0] * len(auxcoef)
  cnt = 0
  while cnt < len(auxcoef):
    for i in range(len(pol1)):
      for j in range(len(pol2)):
        auxcoef[cnt] = pol1[i]*pol2[j]
        auxexp[cnt] = i + j
        cnt = cnt + 1
  cont = 0
#Para sacar cantidad de terminos nulos
  for i in range(len(auxcoef)):
    if auxcoef[i] != 0:
      cont = cont + 1
  prod = [0] * cont
  expp = [0] * cont
  contador = 0
  for i in range(len(auxcoef)):
    if auxcoef[i] == 0:
      continue
    else:
      prod[contador] = auxcoef[i]
      expp[contador] = auxexp[i]
      contador = contador + 1
  return prod

def Valor_deFx(x, polinomio):  # Valor de x y F(x)
  fx = 0
  if (len(polinomio) == 1):
    fx = polinomio[0]
  else:
    for j in range(len(polinomio)):
      if (j == 0):
        fx = fx + polinomio[0]
      else:
        fx = fx + (polinomio[j] * (x ** j))
  return fx


def integrapol(polinomio, a, b):  # a=lim inferior, b=lim sup, n=cantidad de triángulos a trazar
  n = 1000000
  Dx = (b - a) / n  # Base de los rectangulos
  suma = 0  # Acumulador del valor de las áreas de los rectangulos
  x = a  # Valor Inicial que tomará x
  for i in range(n):
    fx = Valor_deFx(x, polinomio)
    altura = fx  # la altura del rectángulo es el valor que posee en y=fx
    Area = Dx * altura  # area del rectángulo
    suma = suma + Area
    x = x + Dx  # nuevo valor de x
  return suma

#Funcion para graficar el polinomio
def graficapol(polinomio):

    ### ARMAR POLINOMIO PARA PODER REMPLAZAR LOS VALORES ###
    puntos = []  # para almacenar los puntos del eje y
    término = 0
    for x in range(-5, 6):
      operación = 0
      for k in range(len(polinomio)):
        término = polinomio[k] * (x ** k)  # reemplaza la x por [-5, 6)
        operación = término + operación
      puntos.append(operación)  # almacena los valores de y

    ### PARA CREAR EL GRÁFICO ###

    x = range(-5, 6)  # rango de los valores que toma x
    plt.style.use('seaborn')  # tema del gráfico
    plt.plot(x, puntos, marker="$♥$", ls=":")  # crea el gráfico
    plt.axhline(0, color="black", linewidth=3)  # crea el eje x
    plt.axvline(0, color="black", linewidth=3)  # crea el eje y
    plt.xlim(-20, 20)  # rango del eje x que se muestra en el gráfico
    plt.ylim(-20, 20)  # rango del eje y que se muestra en el gráfico

    ###PARA CREAR LA TABLA DE VALORES###

    plt.text(20.5, 13, "X", style="italic")  # x en la tabla de valores
    plt.text(23, 13, "Y", style="italic")  # y en la tabla de valores
    c = 1
    v = 0
    for k in range(-5, 6):
      plt.text(20.5, 12 - c, k)  # columna de los valores de x
      c = c + 2
    a = 1
    for k in range(-5, 6):
      plt.text(23, 12 - a, puntos[v])  # columna de los valores de y
      plt.text(22, 12 - (a), "|")
      a = a + 2
      v = v + 1
    plt.show()  # muestra el gráfico en pantalla


