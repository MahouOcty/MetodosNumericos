
from sympy import *  
init_printing()

def determinant(M):
    return M.det()

x, y, z, u, v, w, p, q, r = symbols('x y z u v w p q r')

A = Matrix([
    [-2.8, 7.3, 10.5],
    [8.5, 7.16, -9.4],
    [-2.35, 8.25, -1.6]
])
B = Matrix([
    [-1.25, 1.475],
    [-0.75, 5.015], 
    [1, -2.85]
])
C = Matrix([
    [2.25, -0.5, 2.75],
    [-1, 0, -10.25]
])
D = Matrix([
    [-2, 2.34, -1],
    [2.25, 13.6, 2.36],
    [-9.3, -5.4, -5.25]
])

ev = 1

print("Matriz A:")
pprint(A)
print("Matriz B:")
pprint(B)
print("Matriz C")
pprint(C)
print("Matriz D")
pprint(D)


while (ev != 0):
    ev = eval(input("Ingrese la operacion a realizar, si desea salir ingrese 0: "))
    pprint(ev)