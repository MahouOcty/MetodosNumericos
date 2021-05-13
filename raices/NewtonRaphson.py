from sympy import sin, cos, tan, cot, exp, ln, re, pi, Symbol, diff, sqrt
import numpy as np
import matplotlib.pyplot as plt
from sympy.functions import sign
from sympy import sympify

class NewtonRaphson:
    
    def __init__(self, xi, cant, tolerancia, f):
        self.xi = float(xi)
        self.cant = int(cant)
        self.tolerancia = float(tolerancia)
        self.f = lambda x: eval(f)
        self.df = lambda x: eval(str(diff(f)))
        pass
 
    def newtonRaphson(self):
        step = 1
        flag = 1
        condition = True
        while condition:
            if self.df(self.xi) == 0.0:
                print('divicion entre 0 error')
                break
            
            x1 = float(self.xi - float(self.f(self.xi))/float(self.df(self.xi)))
            print('Iteracion-%d, x1 = %0.6f y f(x1) = %0.6f' % (step, x1, float(self.f(x1)) ))
            self.xi = x1
            step = step + 1
            
            if step > self.cant:
                flag = 0
                break
            
            condition = abs(float(self.f(x1))) > self.tolerancia
        
        if flag==1:
            return ('%0.13f' % x1)
        else:
            return ('\nNo converge.')

f = input('Ingrese la funcion a evaluar: ')
xi = input('Ingrese el valor inicial: ')
tol = input('Ingrese la tolerancia: ')
obj = NewtonRaphson(xi, 50, tol, f)
print(obj.newtonRaphson())
