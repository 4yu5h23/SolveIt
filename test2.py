from sympy import Matrix
M = Matrix(3, 3, [8,-8,-2,4,-3,-2,3,-4,1])
print(M.eigenvects())
print()
print()
eigens = M.eigenvects()

for item in eigens:
    eigenvalue, multiplicity, eigenvector_list = item
    for vec in eigenvector_list:
        for value in vec:
            print(value)
