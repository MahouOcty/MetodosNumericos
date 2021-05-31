
from math import log
from numpy import * 
from matplotlib import pyplot as plt

class Biseccion:
    def __init__(self, f, a, b, tol, imax = 50):
        self.a = a
        self.b = b
        self.tol = tol
        self.Fs = str(f).replace("**", "^").replace("*", "")
        self.f = lambda x: eval(f)
        self.imax = imax
        pass

    def Calculo(self):
        a = self.a
        b = self.b
        r = a
        r1 = b
        error = 1
        i = 0
        while ((i < self.imax) and (error >= self.tol)):
            
            r1 = r
            r = (a+b)/2
            fa = self.f(a)
            fb = self.f(b)
            fr = self.f(r)

            print ('*{:0>2d}'.format(i),'* {:.3f}'.format(a), '* {:.3f}'.format(b), '* {:.3f}'.format(fa), '* {:.3f}'.format(fb), '* {:.3f}'.format(r), '* {:.3f}'.format(fr), '*  {:.3f}'.format(error),' *')
            if (self.f(a)*self.f(r) < 0):
                b = r
            else:
                a = r
            i = i + 1
            error = abs ((r1-r)/r)
        return r

        

def ln(x):
    return log(x)


def regla_falsa(f, a, b, tol, imax=50):
    print('Metodo de biseccion: ')
    print ('***************************************************************')
    print ('* i *   a   *   b   *  f(a) *  f(b) *  ri   * f(rn) *  error  *')

    i = 0
    r = a
    r1 = b
    error = 1

    while ((i < imax) and (error >= tol)):
            
        r1 = r
        r = (b - f(b) * (a-b)/(f(a)-f(b)))

        print ('*{:0>2d}'.format(i),'* {:.3f}'.format(a), '* {:.3f}'.format(b), '* {:.3f}'.format(r), '*  {:.3f}'.format(error),' *')
        if (f(a)*f(r) < 0):
            b = r
        else:
            a = r
        i += 1
        error = abs ((r1-r)/r)
        print ('*{:0>2d}'.format(i),'* {:.3f}'.format(a), '* {:.3f}'.format(b), '* {:.3f}'.format(r), '*  {:.3f}'.format(error),' *')
    print ('***************************************')
    print ("raiz: {:.3f}".format(r),"es una buena aproximacio, con un error de: "+error)
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
   r = biseccion(fx, a, b, tol)
   plt.plot(r,fx(r),'or')
   plt.show()

input()