from matplotlib import pyplot as plt
from numpy import *
import random as rand

def ln(x):
    return log(x)

N = int(input('Ingrese la cantidad de funciones a graficar: '))
x = linspace(-10, 10, 1000)

for i in range(N):
    y = lambda x: eval(input('Ingrese la funcion a evaluar: '))
    plt.plot(x, y(x))

plt.grid()
plt.show()
