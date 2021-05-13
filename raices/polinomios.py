import numpy as np
from fractions import Fraction

imax = int(input('Ingrese el grado del polinomio: ')) + 1
p = []
i = 0
n = 0

for i in range(imax):
    istr = str(imax-1-i)
    ninput = input('Ingrese el indice del termino de grado '+istr+': ')
    n = float(Fraction(ninput))
    p.insert(i,n)


roots = np.roots(p)
stringroot = ''
i = 0
for i in range(imax-1):
    stringroot = str(roots[i])
    print('raiz',(i+1),': ',stringroot.replace('j','i'))
    
input()