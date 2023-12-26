from matrix import Matrix

arr = [[2, 4, 1], [0, 2, 1], [2, 1, 1]]
m1 = Matrix(arr)
mE3 = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
mO3 = Matrix([[0, 0, 0], [0, 0, 0], [0, 0, 0]])

m4 = Matrix([[1, 2, 3], [1, 0, -1]])

m5 = Matrix([[3, 4, 5], [6, 0, -2], [7, 1, 8]])

m2 = Matrix(arr)
print(m1.checkEqual(m2))