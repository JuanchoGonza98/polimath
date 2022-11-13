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
####FUNCIÓN LEEPOL####
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
    if not x and sign=="-":
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



#función para la impresión de un polinomio
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
####FUNCIÓN SUMAPOL####
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


####FUNCIÓN MULPOL####
#funcion que recibe 2 listas y retorna otra lista que contiene la multiplicación de las listas recibidas
def multpol(pol1,pol2):
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
  return formatPoli(prod,expp)


#funcion que retorna el valor de una funcion f(x)
def Valor_deFx(x, polinomio):  # Valor de x y F(x)
  fx = 0
  if (len(polinomio) == 1):
    fx = polinomio[0]
  else:
    for j in range(len(polinomio)):
      if (j == 0):
        fx = fx + polinomio[j]
      else:
        fx = fx + (polinomio[j] * (x ** j))
  return fx

####FUNCIÓN INTEGRAPOL####
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


####FUNCIÓN GRAFICAPOL####
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


####FUNCIÓN RAICESPOL####
def raicespol(polinomio, x1, x2):

    divisores= [] #para almacenar los divisores del término independiente
    sum= [] #almacena las sumas que se van realizando con la regla de Ruffini
    raiz= [] #almacena las raices
    ### CALCULA LAS RAICES DE UN POLINOMIO DE 2DO GRADO ###
    if len(polinomio) == 3 and polinomio[-1] != 0: #verifica si el polinomio es de 2do grado
            determinante= (polinomio[1])**2 - (4 * polinomio[0] * polinomio[2]) #valor de la determinante
            if determinante < 0: #si la determinante es negativa el polinomio no tiene raices
                print('El polinomio no tiene raices reales.')
            if determinante > 0: 
                r1= (-1 * polinomio[1] + (determinante) ** (1/2)) / (2 * polinomio[2]) #halla el valor de una de las raices
                r2= (-1 * polinomio[1] - (determinante) ** (1/2)) / (2 * polinomio[2]) #halla el valor de una de las raices
                if x1 <= r1 <= x2: #verifica si la raiz esta dentro del intervalo [x1, x2]
                    raiz.append(r1)
                if x1 <= r2 <= x2: #verifica si la raiz esta dentro del intervalo [x1, x2]
                    raiz.append(r2)

    if polinomio[0] == 0: #en caso que el polinomio no tenga término independiente o que los otros grados menores al grado mayor sean cero
      for k in range(len(polinomio)):
        if polinomio[k] == 0:
          a= polinomio[k+1]
        elif polinomio[k+1] !=0:
          break 

      if a > 0: #si el coeficiente es positivo
        for d in range(a*-1, a+1 ): 
            if d!= 0 and a % d == 0 :
                divisores.append(d)  
      if a < 0 : #si el coeficiente es negativo
        a= a*-1
        for d in range(a*-1, a+1 ): 
              if d!= 0 and a % d == 0 :
                  divisores.append(d)
        a= a*-1
    ### HALLA LOS DIVISORES DEL TERMINO INDEPENDIENTE ###
    if polinomio[0] < 0: #Si es negativo el término independiente se cambia el signo para que pueda encontrar los divisores
        a= polinomio[0] * -1 #se guarda en una variable para no alterar el signo original 
        for d in range(a*-1, a+1 ): #genera números desde el negativo al positivo ej.: si el término es 6 el rango es de [-6,6]
            if d!= 0 and polinomio[0] % d == 0 : #examina si el número es divisor 
                divisores.append(d)
    else: #si es positivo el término independiente
        for d in range(polinomio[0]*-1, polinomio[0]+1 ): 
            if d!= 0 and polinomio[0] % d == 0 :
                divisores.append(d)

    raiz1=[] #alamacena las raices al remplazar en el polinomio
    término= 0
    ### REEMPLAZAR LOS VALORES DE LOS DIVISORES DEL TÉRMINO INDEPENDIENTE EN EL POLINOMIO, SI DA 0 ES UNA RAIZ###
    for x in divisores: #agarra los divisores
        operación= 0
        for k in range(len(polinomio)):
            término= polinomio[k] * (x ** k) #remplaza el valor de x en cada término
            operación= término + operación   #almacena los términos
        if operación == 0: #si al reemplazar un valor el polinomio es igual a 0 entonces ese valor se almacena como raiz 
            raiz1.append(x) 
    ### SE EVALUA LOS DIVISORES EN LA REGLA DE RUFFINI###
    for n in range(len(raiz1)): #toma los divisores

        qo= int(polinomio[-1]) #término de mayor grado
        sum=[]
        sum.append(qo) #almacena el coeficiente del término de mayor grado
        #       | p0  p1     p2     p3
        #     d |     q0.d  q1.d  q2.d   
        #    _____________________________
        #       |q0   q1      q2    q3
        for i in range(2, len(polinomio) + 1 ): #se empieza en 2 para poder agarrar el penúltimo elemento de la lista que seria el segundo término del polinomio
            qu= polinomio[i*-1] + qo * raiz1[n] #suma los coeficientes con la multiplicacion del resultado por el divisor
            qo= qu #pasa al siguiente coeficiente
            sum.append(qo) #almacena la operación

            if sum[-1] == 0: #si la ultima suma es 0 entonces se extrae el utltimo término y resta un grado al polinomio
                sum.pop(-1)
                for e in range(len(sum)):
                    sum= sum[-1:] + sum[:-1] #desplaza los coeficientes de manera que el índice sea igual al grado del término
                polinomio= sum #la lsita desplazada es el nuevo polinomio
                if x1 <= raiz1[n] <= x2: #si la raiz esta dentro del intervalo de [x1, x2] se almacena ese valor en la lista de raices
                    raiz.append(raiz1[n])
                if len(raiz1) == 1: # si el polinomio se queda con un término entonces se corta el ciclo
                  break

        if len(polinomio) == 3 and polinomio[-1] != 0: #si al polinomio reducido es de 2do grado
            determinante= (polinomio[1])**2 - (4 * polinomio[0] * polinomio[2])
            if determinante > 0:
                r1= (-1 * polinomio[1] + (determinante) ** (1/2)) / (2 * polinomio[2])
                r2= (-1 * polinomio[1] - (determinante) ** (1/2)) / (2 * polinomio[2])
                if x1 <= r1 <= x2 and r1 not in raiz: #se verifica que la raiz este dentro del intervalo introducido por el usuario
                    raiz.append(r1)
                if x1 <= r2 <= x2 and r2 not in raiz: #se verifica que la raiz este dentro del intervalo introducido por el usuario
                    raiz.append(r2)
            break

        if len(polinomio) == 2 and polinomio[-1] != 0: #si el polinomio reducido es de primer grado
            X= (polinomio[-1]*-1) / polinomio[0] #se despeja la x
            if x1 <= x <= x2 and x not in raiz: #se verifica que la raiz este dentro del intervalo introducido por el usuario
                raiz.append(X)
            break

        if len(polinomio) == 1: #si el polinomio se queda con un término 
          x= 0 / polinomio[0]
          if x1 <= x <= x2 and x not in raiz:
            raiz.append(int(x))
          break

    for r in range(len(raiz)): #imprime las raices según el intervalo dado por el usuario
        print("x= ", raiz[r])
        
    return raiz



####FUNCIÓN MAXMINPOL####
def maxminpol(polinomio, x1, x2):
  fx1 = Valor_deFx(x1, polinomio)
  fx2 = Valor_deFx(x2, polinomio)
  primDer = []
  raices = []
  primDer = derivapol(polinomio)  # guarda la derivada del polinomio al hacer la llamada a derivapol
  Valores = []  # guarda los valores de fx entre el intervalo[x1, x2]
  raices = raicespol(primDer, x1, x2)  # obtiene las raices de la primera derivada

  # obtiene el valor de fx1 y fx2; y se almacena entre los valores

  Valores.append(fx1)
  Valores.append(fx2)

  for i in range(len(raices)):
      if (raices[i] != x1 and raices[i] != x2):  # se valida que las raices no sean los extremos ya que han sido agregadas a las  lista de valores previamente
        fx = Valor_deFx(raices[i], polinomio)
        Valores.append(fx)  # se agregan los valores que tiene fx
  minimo = min(Valores) #obtiene el valor minimo de fx
  maximo = max(Valores)#obtiene el valor maxiomo de fx

  for i in range(len(raices)):
    if (Valor_deFx(raices[i], polinomio) == maximo):
      xmax = raices[i]
    if (Valor_deFx(raices[i], polinomio) == minimo):
      minx = raices[i]

    # Comprobando si uno de los extremos es el maximo o el minimo
  if (fx1 == minimo):
    minx = x1
  if (fx1 == maximo):
    xmax = x1
  if (fx2 == minimo):
      minx = x2
  if (fx2 == maximo):
    xmax = x2

  return maximo, xmax, minimo, minx


def es_entero(x): #Verifica que sea un entero
  try:
    int(x)
    return True
  except:
    return False

def format(coef: int, exp: int) -> str: ##Formato de salida para la multiplicación
  if (coef == 0):
    return ""

  if (exp == 0):
    return str(coef)

  result = ""

  if (exp >= 1 and abs(coef) != 1):
    result += str(abs(coef))

  result += "x"

  if (exp > 1):
    result += f"^{exp}"

  return result


def formatPoli(coefs, exps):
  result = ""
  for i in range(len(coefs)):
    formatted = format(coefs[i], exps[i])
    sign = "+" if coefs[i] >= 0 else "-"

    if len(formatted):
      result += f"{sign} {formatted} "

  return result

def verifpol(lista):
  if len(lista) > 13: #Esta funcion retorna 0 si el polinomio es invalido y 1 si es valido
    return 0
  else:
    return 1