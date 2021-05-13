from sympy import sin, cos, tan, cot, exp, ln, re, pi, Symbol, diff, sqrt
import numpy as np



class Montecarlo:
   
    def __init__(self, xi, xf, N, f):
        self.xi = float(xi)
        self.xf = float(xf)
        self.Fs = str(f).replace("**", "^").replace("*", "")
        self.f = lambda x: eval(f)
        self.N = int(N)
        pass

    def calculo(self):
        xrand = np.random.uniform(self.xi, self.xf, self.N)

        integral = 0
        for i in range(self.N):
            integral = integral + self.f(xrand[i])

        respuesta = (self.xf-self.xi)/float(N)*integral
        return respuesta
    pass

xi = input("ingrese punto inicial: ")
xf = input("ingrese punto final: ")
N = input("ingrese cantidad de puntos a calcular: ")
f = input("ingrese funcion: ")

calculo = Montecarlo(xi, xf, N, f)
print("La area calculada al azar tiene un valor de: ", calculo.calculo())
