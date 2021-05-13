from matplotlib import pyplot as plt
from sympy import *

def crearFuncion():
    x = Symbol('x')
    yfun = eval (input('Ingrese la funcion a evaluar: '))
    return yfun

def crearDerivada(y):
    x = Symbol('x')
    ypfun = y.diff(x)
    return ypfun

def segundaDerivada(y):
    x = Symbol('x')
    ypfun = y.diff(x, 2)
    return ypfun


y = crearFuncion()
x = float(input('Ingrese el valor a evaluar: '))
ystr = str(y)
f = lambda x: eval(ystr)

yp = crearDerivada(y)
ypstr = str(yp)
fp = lambda x: eval(ypstr)
print('primera derivada:',yp)
print(fp(x))

ypp= segundaDerivada(y)
yppstr = str(ypp)
fpp = lambda x: eval(yppstr)
print('segunda derivada:',ypp)
print(fpp(x))

input()