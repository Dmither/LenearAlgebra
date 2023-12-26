from matrix import Matrix

arr = [[2, 4, 1], [0, 2, 1], [2, 1, 1]]
m1 = Matrix(arr)
mE3 = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
mO3 = Matrix([[0, 0, 0], [0, 0, 0], [0, 0, 0]])

print(m1.getDeterminante())

m2 = Matrix([[2, 4, 1, 1],
             [0, 2, 0, 0],
             [2, 1, 1, 3],
             [4, 0, 2, 3]])

print(m2.getDeterminante())

m3 = Matrix([[2, -3, 1],
             [4, -5, 2],
             [5, -7, 3]])

print(m3)
print(m3.getReverse())