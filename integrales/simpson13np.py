from numpy import *
import scipy.integrate as spi

'''def simps(f,a,b,N):
    dx = (b-a)/N
    x = np.linspace(a,b,N+1)
    y = f(x)
    S = dx/3 * np.sum(y[0:-1:2] + 4*y[1::2] + y[2::2])
    return S'''


f = input('Ingrese la funcion a evaluar: ')
a = float(input('Ingrese el valor inferior: '))
b = float(input('Ingrese el valor superior: '))

N = int(input('Ingrese el numero de particiones: '))


x = linspace(a,b,N+1)
y = eval(f)
approximation = spi.simps(y,x)
print(approximation)