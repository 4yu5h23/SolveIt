import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from sympy import *

LARGEFONT = ("Times New Roman", 20)


class tkinterApp(tk.Tk):

    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        # creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, Page1, Page2 , Page3,):
            frame = F(container, self)

            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


# first window frame startpage

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # label of frame Layout 2
        label = ttk.Label(self, text="Engineering Mathematics Calculator", font=LARGEFONT, anchor="center")

        # putting the grid in its place by using
        # grid
        label.grid(row=0, column=2, padx=200, pady=10)

        button1 = ttk.Button(self, text="Eigenvalues and Eigenvectors",
                             command=lambda: controller.show_frame(Page1))

        # putting the button in its place by
        # using grid
        button1.grid(row=1, column=2, padx=10, pady=10)

        ## button to show frame 2 with text layout2
        button2 = ttk.Button(self, text="Integration",
                             command=lambda: controller.show_frame(Page2))

        # putting the button in its place by
        # using grid
        button2.grid(row=2, column=2, padx=10, pady=10)

        button3 = ttk.Button(self, text="Differentiation",
                                command=lambda: controller.show_frame(Page3))

        button3.grid(row=3, column=2, padx=10, pady=10)


# second window frame page1
class Page1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Eigen values and vectors", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)



        def calculate_eigen():
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


        # Create labels for matrix elements
        label_matrix = tk.Label(self, text="Enter Matrix Elements:")
        label_matrix.grid(row=0, column=0, columnspan=3)

        label_a1 = tk.Label(self, text="a1:")
        label_a1.grid(row=1, column=0)
        label_b1 = tk.Label(self, text="b1:")
        label_b1.grid(row=1, column=1)
        label_c1 = tk.Label(self, text="c1:")
        label_c1.grid(row=1, column=2)

        label_a2 = tk.Label(self, text="a2:")
        label_a2.grid(row=2, column=0)
        label_b2 = tk.Label(self, text="b2:")
        label_b2.grid(row=2, column=1)
        label_c2 = tk.Label(self, text="c2:")
        label_c2.grid(row=2, column=2)

        label_a3 = tk.Label(self, text="a3:")
        label_a3.grid(row=3, column=0)
        label_b3 = tk.Label(self, text="b3:")
        label_b3.grid(row=3, column=1)
        label_c3 = tk.Label(self, text="c3:")
        label_c3.grid(row=3, column=2)

        # Create entry fields for matrix elements
        entry_a1 = tk.Entry(self)
        entry_a1.grid(row=1, column=3)
        entry_b1 = tk.Entry(self)
        entry_b1.grid(row=1, column=4)
        entry_c1 = tk.Entry(self)
        entry_c1.grid(row=1, column=5)

        entry_a2 = tk.Entry(self)
        entry_a2.grid(row=2, column=3)
        entry_b2 = tk.Entry(self)
        entry_b2.grid(row=2, column=4)
        entry_c2 = tk.Entry(self)
        entry_c2.grid(row=2, column=5)

        entry_a3 = tk.Entry(self)
        entry_a3.grid(row=3, column=3)
        entry_b3 = tk.Entry(self)
        entry_b3.grid(row=3, column=4)
        entry_c3 = tk.Entry(self)
        entry_c3.grid(row=3, column=5)

        # Create button to calculate eigen values and vectors
        button_calculate = tk.Button(self, text="Calculate Eigen Values and Vectors", command=calculate_eigen)
        button_calculate.grid(row=4, column=0, columnspan=6)

        # Create label for results
        results_label = tk.Label(self, text="")
        results_label.grid(row=5, column=0, columnspan=6)

        entry_a1.focus()
        entry_a1.bind("<Return>", lambda funct1: entry_b1.focus())
        entry_b1.bind("<Return>", lambda funct1: entry_c1.focus())
        entry_c1.bind("<Return>", lambda funct1: entry_a2.focus())
        entry_a2.bind("<Return>", lambda funct1: entry_b2.focus())
        entry_b2.bind("<Return>", lambda funct1: entry_c2.focus())
        entry_c2.bind("<Return>", lambda funct1: entry_a3.focus())
        entry_a3.bind("<Return>", lambda funct1: entry_b3.focus())
        entry_b3.bind("<Return>", lambda funct1: entry_c3.focus())
        entry_c3.bind("<Return>", lambda funct1: button_calculate.focus())

        button_calculate.bind("<Shift_R>", lambda funct1: entry_c3.focus())
        entry_c3.bind("<Shift_R>", lambda funct1: entry_b3.focus())
        entry_b3.bind("<Shift_R>", lambda funct1: entry_a3.focus())
        entry_a3.bind("<Shift_R>", lambda funct1: entry_c2.focus())
        entry_c2.bind("<Shift_R>", lambda funct1: entry_b2.focus())
        entry_b2.bind("<Shift_R>", lambda funct1: entry_a2.focus())
        entry_a2.bind("<Shift_R>", lambda funct1: entry_c1.focus())
        entry_c1.bind("<Shift_R>", lambda funct1: entry_b1.focus())
        entry_b1.bind("<Shift_R>", lambda funct1: entry_a1.focus())

        button_calculate.bind("<Return>", lambda funct1: calculate_eigen())


        back_button = tk.Button(self, text="Back", command=lambda: controller.show_frame(StartPage))
        back_button.grid(row=6, column=0, columnspan=6)
# third window frame page2
class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Integration", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        def find_integral():
            try:
                # Get user input from text boxes
                function_str = function_entry.get()
                variable_str = variable_entry.get()

                # Parse user input
                function_expr = sympify(function_str)
                variable = symbols(variable_str)

                # Find integral
                integral = integrate(function_expr, variable)

                # Update result label
                result_label.config(text=f"Integral: {integral}")

            except Exception as e:
                messagebox.showerror("Error", str(e))

        # Function label and entry
        function_label = tk.Label(self, text="Function:")
        function_label.grid(row=2, column=0)
        function_entry = tk.Entry(self)
        function_entry.grid(row=2, column=1)

        # Variable label and entry
        variable_label = tk.Label(self, text="Variable:")
        variable_label.grid(row=3, column=0)
        variable_entry = tk.Entry(self)
        variable_entry.grid(row=3, column=1)

        # Button to calculate integral
        calculate_button = tk.Button(self, text="Calculate", command=find_integral)
        calculate_button.grid(row=4, column=0, columnspan=2)

        # Result label
        result_label = tk.Label(self, text="")
        result_label.grid(row=5, column=0, columnspan=2)

        back_button = tk.Button(self, text="Back", command=lambda: controller.show_frame(StartPage))
        back_button.grid(row=6, column=0, columnspan=6)


class Page3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Differentiation", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        def calculate_derivative():
            function = function_entry.get()
            variable = variable_entry.get()

            try:
                x = Symbol(variable)
                f = sympify(function)
                derivative = diff(f, x)
                derivative_label.config(
                    text=f"The derivative of {function} with respect to {variable} is: {derivative}")
            except:
                derivative_label.config(text="Error: Invalid input!")


        # Create input fields for function and variable
        function_label = tk.Label(self, text="Enter function:")
        function_label.grid(row=2, column=0)
        function_entry = tk.Entry(self)
        function_entry.grid(row=2, column=1)

        variable_label = tk.Label(self, text="Enter variable:")
        variable_label.grid(row=3, column=0)
        variable_entry = tk.Entry(self)
        variable_entry.grid(row=3, column=1)

        # Create "Calculate" button
        calculate_button = tk.Button(self, text="Calculate", command=calculate_derivative)
        calculate_button.grid(row=4, column=0, columnspan=2)

        # Create label to display derivative
        derivative_label = tk.Label(self, text="")
        derivative_label.grid(row=5, column=0, columnspan=2)

        back_button = tk.Button(self, text="Back", command=lambda: controller.show_frame(StartPage))
        back_button.grid(row=6, column=0, columnspan=6)
app = tkinterApp()
app.mainloop()
