from funciones import *
def derivapol(F):
    for j in range(len(F)):
        F[j] = j * F[j]
    der = [0] * (len(F) - 1)
    for i in range(len(F)-1):
        der[i] = F[i+1]
    return der
print("Ingrese el polinomio: ")
polinomio = leepol(input())
print("La derivada es: ",Representacion_poli(derivapol(polinomio)))
