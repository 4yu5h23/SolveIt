
import sympy as sp
from sympy import *
import numpy as np
import tkinter as tk
from tkinter import *

def calculate_eigen(a1, b1, c1, a2, b2, c2, a3, b3, c3):
    # Get matrix elements from input fields
    try:
        a1 = int(entry_a1.get())
        b1 = int(entry_b1.get())
        c1 = int(entry_c1.get())

        a2 = int(entry_a2.get())
        b2 = int(entry_b2.get())
        c2 = int(entry_c2.get())

        a3 = int(entry_a3.get())
        b3 = int(entry_b3.get())
        c3 = int(entry_c3.get())

        # trace of matrix
        tr = [a1 + b2 + c3]
        # print("Trace of matrix :", tr)

        # sum of minors of a1,b2,c3

        sm = [(b2 * c3 - b3 * c2) + (a1 * c3 - a3 * c1) + (a1 * b2 - a2 * b1)]
        # print("sum of minors of a1,b2,c3 :", sm)

        # determinant of Matrix

        detM = a1 * (b2 * c3 - b3 * c2) - b1 * (a2 * c3 - a3 * c2) + c1 * (a2 * b3 - a3 * b2)
        # print("Determinant of the Matrix is :", detM)

        # print characteristic equation
        # print("The characteristic Equation :" + "\u03BB" + "\u00b3" + " -", tr, "\u03BB" + "\u00b2" + " +", sm,"\u03BB" + " -",detM)

        # \u03BB is lambda
        # \u00b3 is cube
        # \u00b2 is square
        print()
        print()
        # eigen values and vectors using sympy
        import sympy as sp
        from sympy import Matrix
        M = Matrix([[a1, b1, c1], [a2, b2, c2], [a3, b3, c3]])

        vals = M.eigenvals()

        if len(vals) == 3:
            # print("the eigen values are distinct\n")
            valslist = list(vals.keys())
            # print("The Eigen values are:")
            print(valslist[0])
            print(valslist[1])
            print(valslist[2])

            eval1 = valslist[0]
            eval2 = valslist[1]
            eval3 = valslist[2]

            # for eval1
            # print("The possible sets of eigen vectors for eigen value=", eval1, "are:")
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
            # print("The possible sets of eigen vectors for eigen value=", eval2, "are:")
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
            # print("The possible sets of eigen vectors for eigen value=", eval3, "are:")
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

        vals = M.eigenvals()
        if len(vals) == 2:
            eigenvalue_distinctness = "Not distinct"
        if len(vals) == 3:
            eigenvalue_distinctness = "Distinct"

        results_label.configure(text=
                                f"Trace: {tr}\n\n"
                                f"Sum of minors of a1 ,b2 ,c3: {sm}\n\n"
                                f"Determinant: {detM}\n\n"
                                f"Characteristic Equation: \u03BB \u00b3 - {tr} \u03BB \u00b2 + {sm} \u03BB  - {detM} \n\n"
                                f"Eigenvalues: {eval1}, {eval2},and {eval3} \n\n"
                                f"Eigenvalue Distinctness: {eigenvalue_distinctness}\n\n"
                                f"Possible Set of Eigenvectors \n For Eigen Value : {eval1} :\n{vect1}, \n {vect2},\n {vect3},\n\n For Eigen Value {eval2} \n{vect4},\n {vect5},\n {vect6}, \n\n For Eigen Value {eval3} \n {vect7},\n {vect8},\n {vect9}\n")
    except Exception as e:
        messagebox.showerror("Error", str(e))
