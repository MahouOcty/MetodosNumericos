from numpy import *
from matplotlib import pyplot as plt

def ln(x):
    return log(x)

def regla_falsa(f, a, b, tol, imax=50):
    print('Metodo de falsa regla: ')
    print ('************************************************************************')
    print ('* i *   a    *   b    *   f(a)  *   f(b) *   ri   *  f(ri)  *   error  *')

    i = 0
    r = a
    r1 = b
    error = 1
    fa = f(a)
    fb = f(b)
    fr = f(r)

    while ((i < imax) and (error > tol)):
            
        r1 = r
        r = (b - f(b) * (a-b)/(f(a)-f(b)))
        error = abs ((r1-r)/r)

        print ('*{:0>2d}'.format(i),'* {:.4f}'.format(a), '* {:.4f}'.format(b), '* {:.4f}'.format(fa), '* {:.4f}'.format(fb), '* {:.4f}'.format(r), '* {:.4f}'.format(fr), '*  {:.4f}'.format(error),' *')
        if (f(a)*f(r) < 0):
            b = r
        else:
            a = r
        i += 1
        error = abs ((r1-r)/r)
    print ('************************************************************************')
    print ("raiz: {:.6f}".format(r),"es una buena aproximacion, con un error de: ",error)
    print(' ')
    return r

f = input('Ingrese la funcion a evaluar: ')
fx = lambda x: eval(f)
r = 0
a = float(input('Ingrese el limite inferior: '))
b = float(input('Ingrese el limite superior: '))
tol = float(input('Ingrese el error relativo: '))
xgraph = linspace(a, b, 100)
plt.plot(xgraph, fx(xgraph))
plt.grid()
print(' ')


if (fx(a) * fx(b) > 0):
    print ("El programa no puede identificar si existe un corte al ambos puntos ser del mismo signo")
else:
    r = regla_falsa(fx, a, b, tol)
    plt.plot(r,fx(r),'or')
    plt.show()

input()