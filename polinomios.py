import re
def coefs(entrada):
  regexp = r"(-?\d*)(x?)(?:(?:\^|\*\*)(\d))?"
  c = {}
  for coef, x, exp in re.findall(regexp, entrada):
    # print(coef, x, exp)
    if not coef and not x:
      continue
    if x and not coef:
      coef = '1'
    if x and coef == "-":
      coef = "-1"
    if x and not exp:
      exp = '1'
    if coef and not x:
      exp = '0'
    exp = ord(exp) & 0x000F
    c[exp] = float(coef)
  grado = max(c)
  coeficientes = [0.0] * (grado+1)
  for g, v in c.items():
    coeficientes[g] = v
  return coeficientes
while True:
    print("Menu de opciones")
    print("1-Suma de polinomios")
    print("0-Salir")
    opc = int(input("Ingrese su opcion: "))
    if opc == 1:
      sumapol()
    if opc == 0:
      break

def sumapol():
  print("Ingrese el valor de los polinomios a sumar: ")
  print("P(x): ")
  pol1 = coefs(input())
  print("Q(x): ")
  pol2 = coefs(input())
  for i in range(len(pol1)):
