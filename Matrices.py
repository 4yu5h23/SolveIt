

def traceofmatrix(M: list)->int:
    a1 = int(M[0][0])
    b2 = int(M[1][1])
    c3 = int(M[2][2])
    return a1 + b2 + c3


def sumofminors(M: list)->int:
    a1 = int(M[0][0])
    b1 = int(M[0][1])
    c1 = int(M[0][2])

    a2 = int(M[1][0])
    b2 = int(M[1][1])
    c2 = int(M[1][2])

    a3 = int(M[2][0])
    b3 = int(M[2][1])
    c3 = int(M[2][2])
    return (b2 * c3 - b3 * c2) + (a1 * c3 - a3 * c1) + (a1 * b2 - a2 * b1)




def determinantofmatrix(N: list)->int:
    a1 = int(N[0][0])
    b1 = int(N[0][1])
    c1 = int(N[0][2])

    a2 = int(N[1][0])
    b2 = int(N[1][1])
    c2 = int(N[1][2])

    a3 = int(N[2][0])
    b3 = int(N[2][1])
    c3 = int(N[2][2])
    return a1 * (b2 * c3 - b3 * c2) - b1 * (a2 * c3 - a3 * c2) + c1 * (a2 * b3 - a3 * b2)

def characteristiceqn(M: list)->str:
    tr = traceofmatrix(M)
    sm = sumofminors(M)
    detM = determinantofmatrix(M)
    chareqn = "\u03BB"+"\u00b3"+" - "+str(tr)+"\u03BB"+"\u00b2"+" + "+str(sm)+"\u03BB"+" - "+str(detM)
    return chareqn
import sympy
from sympy import Matrix


def  eigenvals(N: list)->list :
    a1 = int(N[0][0])
    b1 = int(N[0][1])
    c1 = int(N[0][2])

    a2 = int(N[1][0])
    b2 = int(N[1][1])
    c2 = int(N[1][2])

    a3 = int(N[2][0])
    b3 = int(N[2][1])
    c3 = int(N[2][2])

    M = Matrix([[a1, b1, c1], [a2, b2, c2], [a3, b3, c3]])
    vals = M.eigenvals()
    if len(vals) == 3:
        vals = list(vals.keys())
    elif len(vals) == 2:
        vals = list(vals.keys())
        vals.insert(0, vals[0])
    return vals


def eigenvec(N: list, V: int) -> list:
    vects=[]

    a1 = int(N[0][0])
    b1 = int(N[0][1])
    c1 = int(N[0][2])

    a2 = int(N[1][0])
    b2 = int(N[1][1])
    c2 = int(N[1][2])

    a3 = int(N[2][0])
    b3 = int(N[2][1])
    c3 = int(N[2][2])

    x1 = (b2 - V) * (c3 - V) - b3 * c2
    y1 = -1 * (a2 * (c3 - V) - a3 * c2)
    z1 = a2 * b3 - a3 * (b2 - V)
    vect1 = [x1, y1, z1]
    if vect1 != [0,0,0]: vects.append(vect1)

    x2 = b1 * c2 - (b2 - V) * c1
    y2 = -1 * ((a1 - V) * c2 - a2 * c1)
    z2 = (a1 - V) * (b2 - V) - a2 * b1
    vect2 = [x2, y2, z2]
    if vect2 != [0, 0, 0]: vects.append(vect2)

    x3 = b1 * (c3 - V) - b3 * c1
    y3 = -1 * ((a1 - V) * (c3 - V) - a3 * c1)
    z3 = (a1 - V) * b3 - a3 * b1
    vect3 = [x3, y3, z3]
    if vect3 != [0, 0, 0]: vects.append(vect3)

    return vects
