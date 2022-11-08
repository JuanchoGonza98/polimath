import re
#Funcion que recibe string en forma de polinomio kx^n+k1x^n-1........
def leepol(entrada):
  regexp = r"([+-]?)(?:\s*)(\d*)(x?)(?:\^)?(\d+)?" #Se declaran expresiones regulares para diferenciar cada termino,signo,exponente y coeficiente del polinomio
  c = {} #Lista donde se guardaran e iran filtrando de acuerdo al regex
  for sign, coef, x, exp in re.findall(regexp, entrada): #Ciclo for donde se recorre cada termino del polinomios
    # print(f"{sign}, {coef}, {x}, {exp}")
    if not coef and not x:
      continue

    if x and not coef:
      coef = '1'
    if x and sign == "-":
      coef = "-" + coef
    if not x and sign == "-":
      coef = "-" + coef
    if x and not exp:
      exp = '1'
    if coef and not x:
      exp = '0'

    exp = int(exp)
    c[exp] = int(coef)

  grado = max(c)
  coeficientes = [0] * (grado+1)
  for g, v in c.items():
    coeficientes[g] = v
  return coeficientes
######Fin de la funcion leepol
def sumapol(P,Q):
  aux = 0
  if len(P) > len(Q):
    mayor = len(P)
    menor = len(Q)
    sum = [0]*mayor
    for i in range(menor):
      sum[i] = P[i] + Q [i]
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
            elemento = str(entrada[longitud]) + 'x^' + str(longitud)
            aux.append(elemento)
          else:
            elemento = str(entrada[longitud]) + 'x'
            aux.append(elemento)

        if (longitud != n and longitud > 1 and entrada[
          longitud] != 0):  # si es el primer elemeto añadir caracter + en caso de los positivos
          if (entrada[longitud] < 0):
            elemento = str(entrada[longitud]) + 'x^' + str(longitud)
            aux.append(elemento)
          else:
            elemento = '+' + str(entrada[longitud]) + 'x^' + str(longitud)
            aux.append(elemento)
        if (longitud == 1 and entrada[
          longitud] != 0 and longitud != n):  # evitar el caracter ^ cuando el exponente es 1
          if (entrada[longitud] < 0):
            elemento = str(entrada[longitud]) + 'x'
            aux.append(elemento)
          else:
            elemento = '+' + str(entrada[longitud]) + 'x'
            aux.append(elemento)
        if (longitud == 0 and entrada[longitud] != 0):  # evitar la variable x para el termino independiente
          if (entrada[longitud] < 0):
            elemento = str(entrada[longitud])
            aux.append(elemento)
          else:
            elemento = '+' + str(entrada[longitud])
            aux.append(elemento)
        longitud = longitud - 1
    cad = "".join(aux)
    return cad


