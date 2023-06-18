# code to take a 3x3 matrix as input
M = []
print("enter the matrix elements in order")
for i in range(3):
    l = []
    for j in range(3):
        v = int(input())
        l.append(v)
    M.append(l)
# printing the matrix in proper structure
for i in range(3):
    for j in range(3):
        print(M[i][j], end=" ")
    print()

# assigning the elements to easy variables
a1 = int(M[0][0])
b1 = int(M[0][1])
c1 = int(M[0][2])

a2 = int(M[1][0])
b2 = int(M[1][1])
c2 = int(M[1][2])

a3 = int(M[2][0])
b3 = int(M[2][1])
c3 = int(M[2][2])

# trace of matrix
tr = [a1 + b2 + c3]
print("Trace of matrix :", tr)

# sum of minors of a1,b2,c3

sm = [(b2 * c3 - b3 * c2) + (a1 * c3 - a3 * c1) + (a1 * b2 - a2 * b1)]
print("sum of minors of a1,b2,c3 :", sm)

# determinant of Matrix

detM = a1 * (b2 * c3 - b3 * c2) - b1 * (a2 * c3 - a3 * c2) + c1 * (a2 * b3 - a3 * b2)
print("Determinant of the Matrix is :", detM)

# print characteristic equation
print("The characteristic Equation :" + "\u03BB" + "\u00b3" + " -", tr, "\u03BB" + "\u00b2" + " +", sm, "\u03BB" + " -",
      detM)

# \u03BB is lambda
# \u00b3 is cube
# \u00b2 is square
print()
print()
# eigen values and vectors using sympy
import sympy as sp
from sympy import *

M = Matrix([[a1, b1, c1], [a2, b2, c2], [a3, b3, c3]])

vals = M.eigenvals()

if len(vals) == 3:
    print("the eigen values are distinct\n")
    valslist = list(vals.keys())
    print("The Eigen values are:")
    print(valslist[0])
    print(valslist[1])
    print(valslist[2])

    eval1 = valslist[0]
    eval2 = valslist[1]
    eval3 = valslist[2]

    # for eval1
    print("The possible sets of eigen vectors for eigen value=", eval1, "are:")
    # case1
    x1 = (b2 - eval1) * (c3 - eval1) - b3 * c2
    y1 = -1 * (a2 * (c3 - eval1) - a3 * c2)
    z1 = a2 * b3 - a3 * (b2 - eval1)
    vect1 = [x1, y1, z1]
    print(vect1)

    # case2
    x2 = b1 * c2 - (b2 - eval1) * c1
    y2 = -1 * ((a1 - eval1) * c2 - a2 * c1)
    z2 = (a1 - eval1) * (b2 - eval1) - a2 * b1
    vect2 = [x2, y2, z2]
    print(vect2)

    # case3
    x3 = b1 * (c3 - eval1) - b3 * c1
    y3 = -1 * ((a1 - eval1) * (c3 - eval1) - a3 * c1)
    z3 = (a1 - eval1) * b3 - a3 * b1
    vect3 = [x3, y3, z3]
    print(vect3)

    # for eval2
    print("The possible sets of eigen vectors for eigen value=", eval2, "are:")
    # case1
    x4 = (b2 - eval2) * (c3 - eval2) - b3 * c2
    y4 = -1 * (a2 * (c3 - eval2) - a3 * c2)
    z4 = a2 * b3 - a3 * (b2 - eval2)
    vect4 = [x4, y4, z4]
    print(vect4)

    # case2
    x5 = b1 * c2 - (b2 - eval2) * c1
    y5 = -1 * ((a1 - eval2) * c2 - a2 * c1)
    z5 = (a1 - eval2) * (b2 - eval2) - a2 * b1
    vect5 = [x5, y5, z5]
    print(vect5)

    # case3
    x6 = b1 * (c3 - eval2) - b3 * c1
    y6 = -1 * ((a1 - eval2) * (c3 - eval2) - a3 * c1)
    z6 = (a1 - eval2) * b3 - a3 * b1
    vect6 = [x6, y6, z6]
    print(vect6)

    # for eval3
    print("The possible sets of eigen vectors for eigen value=", eval3, "are:")
    # case1
    x7 = (b2 - eval3) * (c3 - eval3) - b3 * c2
    y7 = -1 * (a2 * (c3 - eval3) - a3 * c2)
    z7 = a2 * b3 - a3 * (b2 - eval3)
    vect7 = [x7, y7, z7]
    print(vect7)

    # case2
    x8 = b1 * c2 - (b2 - eval3) * c1
    y8 = -1 * ((a1 - eval3) * c2 - a2 * c1)
    z8 = (a1 - eval3) * (b2 - eval3) - a2 * b1
    vect8 = [x8, y8, z8]
    print(vect8)

    # case3
    x9 = b1 * (c3 - eval3) - b3 * c1
    y9 = -1 * ((a1 - eval3) * (c3 - eval3) - a3 * c1)
    z9 = (a1 - eval3) * b3 - a3 * b1
    vect9 = [x9, y9, z9]
    print(vect9)
if len(vals) == 2:
    print("The Eigen values are not distinct\n")
    print("The Eigen values are:")
    print(list(vals.keys())[list(vals.values()).index(1)])
    print(list(vals.keys())[list(vals.values()).index(2)])
    print(list(vals.keys())[list(vals.values()).index(2)])

    eval1 = list(vals.keys())[list(vals.values()).index(1)]
    eval2 = list(vals.keys())[list(vals.values()).index(2)]

    # for eval1
    print("The possible sets of eigen vectors for eigen value=", eval1, "are:")
    # case1
    x1 = (b2 - eval1) * (c3 - eval1) - b3 * c2
    y1 = -1 * (a2 * (c3 - eval1) - a3 * c2)
    z1 = a2 * b3 - a3 * (b2 - eval1)
    vect1 = [x1, y1, z1]
    print(vect1)

    # case2
    x2 = b1 * c2 - (b2 - eval1) * c1
    y2 = -1 * ((a1 - eval1) * c2 - a2 * c1)
    z2 = (a1 - eval1) * (b2 - eval1) - a2 * b1
    vect2 = [x2, y2, z2]
    print(vect2)

    # case3
    x3 = b1 * (c3 - eval1) - b3 * c1
    y3 = -1 * ((a1 - eval1) * (c3 - eval1) - a3 * c1)
    z3 = (a1 - eval1) * b3 - a3 * b1
    vect3 = [x3, y3, z3]
    print(vect3)

    # for eval2
    print("The eigen vectors for eigen value=", eval2, "are:")
    V = M.eigenvects()
    if V[0][1] == 2:
        print(V[0][2][0],"\n")
        print(V[0][2][1],"\n")

    if V[1][1] == 2:
        print(V[1][2][0],"\n")
        print(V[1][2][1],"\n")
