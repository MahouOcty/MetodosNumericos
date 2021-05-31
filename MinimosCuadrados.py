from numpy import polyfit, array, asarray, poly1d, sqrt
from numpy.core.function_base import linspace
from sympy import Symbol, init_printing, pprint
import matplotlib.pyplot as plt

init_printing()

plt.grid(True)

def Polinomios(a, b):
    x = Symbol('x')
    ylen = b.size
    yprom = 0
    for i in range (ylen):
        yprom += b[i]
    
    yprom *= (1/ylen)
    p1 = polyfit(a, b, 1)
    z1 = poly1d(p1)
    print("----------------------------------------")
    print("Polimonio 1: ")
    pprint(p1[0]*x+p1[1])
    Sr1 = 0
    St1 = 0
    for i in range (ylen):
        Sr1 += (b[i]-z1(a[i]))**2
        St1 += (b[i]-yprom)**2
    r1 = sqrt((St1-Sr1)/St1)
    print("Coeficiente =", r1)
    
    p2 = polyfit(a, b, 2)
    z2 = poly1d(p2)
    print("Polimonio 2: ")
    pprint(p2[0]*x**2+p2[1]*x+p2[2])
    Sr2 = 0
    St2 = 0
    for i in range (ylen):
        Sr2 += (b[i]-z2(a[i]))**2
        St2 += (b[i]-yprom)**2
    r2 = sqrt((St2-Sr2)/St2)
    print("Coeficiente =", r2)
    xp = linspace(0, 2)
    _= plt.plot(a, b, ".", xp, z1(xp), "-", xp, z2(xp), "--")
    plt.show()
    p3 = polyfit(a, b, 3)
    pprint(p3[0]*x**3+p3[1]*x**2+p3[2]*x+p3[3])
    p4 = polyfit(a, b, 4)
    pprint(p4[0]*x**4+p4[1]*x**3+p4[2]*x**2+p4[3]*x+p4[4])
    p5 = polyfit(a, b, 5)
    pprint(p5[0]*x**5+p5[1]*x**4+p5[2]*x**3+p5[3]*x**2+p5[4]*x+p5[5])
    p6 = polyfit(a, b, 6)
    pprint(p6[0]*x**6+p6[1]*x**5+p6[2]*x**4+p6[3]*x**3+p6[4]*x**2+p6[5]*x+p6[6])


# Datos experimentales
x = []
y = []
n = int(input("Inserte la cantidad de puntos: "))

for i in range(n):
    print("------------------------------------------")
    x.append(float(input("X"+str(i)+":")))
    y.append(float(input("Y"+str(i)+":")))
# Ajuste a una recta (polinomio de grado 1)
X = asarray(x)
Y = asarray(y)
Polinomios(X, Y)

# imprime [ 2.7   9.94]

