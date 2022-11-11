from funciones import *
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
  return auxcoef

print("Ingrese Q(x): ")
Q = leepol(input())
print("Ingrese P(x): ")
P = leepol(input())
producto = mulpol(Q,P)
print(producto)
print("El prod es: ",Representacion_poli(producto))