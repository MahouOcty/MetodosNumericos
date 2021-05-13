from numpy import *
import math
import matplotlib.pyplot as plt

class secante:

    def Secante(self,x0,x1,tol,N,f):

        print ('**********************************************************************')
        print ('* i *   x1   *   x0   *   f(x1) *  f(x0) *   xr  *  f(xr) *   error  *')
        i=1
        h= 0.00001   
        error = 2*tol
        while i<=N:
            x= x1 - float(f(x1))*(x1-x0)/(float(f(x1))-float(f(x0)))  
            error = abs(x-x1)
            print ('*{:0>2d}'.format(i),'* {:.4f}'.format(x1), '* {:.4f}'.format(x0), '* {:.4f}'.format(f(x1)), '* {:.4f}'.format(f(x0)), '* {:.4f}'.format(x), '* {:.4f}'.format(f(x)), '*  {:.4f}'.format(error),' *')
            if error<tol:
                print ('**********************************************************************')
                print('La solucion es: ',x," con un error de: ",error)
                return x
            i=i + 1
            x0=x1   
            x1=x     
        
llamar=secante()
 
  
## funciona con numpy np para las funciones trigonometricas np.sin()... etc  
f = input("funcion: ")
funcion=lambda x: eval(f)

 
xInicial1= int(input("intervalo A: "))  ## VALOR A
xInicial2= int(input("intervalo B: "))  ## VALLOR B
tolerancia=float(input("tolerancia: "))  ## VALOR DE MAGAÑ A
iteraciones=20   ## ITERACIONES MAGAÑA
    
x=llamar.Secante(xInicial1,xInicial2,tolerancia,iteraciones,funcion)
p= linspace(-5,5,100)
var = []

plt.plot(p, funcion(p))
plt.plot(x,0,'or')
plt.grid()
plt.show()

input()