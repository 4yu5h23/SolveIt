

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
def  eigenvals(N: list)->list       :
    a1 = int(N[0][0])
    b1 = int(N[0][1])
    c1 = int(N[0][2])

    a2 = int(N[1][0])
    b2 = int(N[1][1])
    c2 = int(N[1][2])

    a3 = int(N[2][0])
    b3 = int(N[2][1])
    c3 = int(N[2][2])

