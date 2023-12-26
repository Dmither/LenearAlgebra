class Matrix:
  
  def __init__(self, arr=[[0]]):
    self.rows = len(arr)
    self.cols = len(arr[0])
    self.body = arr
    self.square = self.rows == self.cols
      
  def __str__(self):
    res = ""
    for row in self.body:
      line = " "
      for i in row:
        line += str(i) + " "
      res += ("|" + line + "|\n")
    return res
  
  def add(self, matrix):
    rows = self.rows
    cols = self.cols
    if (rows != matrix.rows or cols != matrix.cols):
      return
    arr = []
    for i in range(rows):
      row = []
      for j in range(cols):
        row.append(self.body[i][j] + matrix.body[i][j])
      arr.append(row)
    return Matrix(arr)

  def mul(self, target):
    rows = self.rows
    cols = self.cols

    if (isinstance(target, int)):
      arr = []
      for i in range(rows):
        row = []
        for j in range(cols):
          row.append(self.body[i][j] * target)
        arr.append(row)
      return Matrix(arr)

    if (cols != target.rows):
      return
    arr = []
    for i in range(rows):
      row = []
      for j in range(cols):
        cell = 0
        for k in range(cols):
          cell += self.body[i][k] * target.body[k][j]
        row.append(cell)
      arr.append(row)
    return Matrix(arr)
  
  def pow(self, n):
    if not self.square:
      return
    res = Matrix(self.body)
    for i in range(n - 1):
      res = res.mul(self)
    return res

  def checkCommutative(self, target):
    mul1 = self.mul(target)
    mul2 = target.mul(self)
    for i in range(mul1.rows):
      for j in range(mul1.cols):
        if (mul1.body[i][j] != mul2.body[i][j]):
          return False
    return True
  
  def checkEqual(self, target):
    if (self.rows != target.rows or self.cols != target.cols):
      return False
    for i in range(self.rows):
      for j in range(self.cols):
        if (self.body[i][j] != self.body[i][j]):
          return False
    return True
  
  def transport(self):
    arr = []
    for i in range(self.cols):
      row = []
      for j in range(self.rows):
        row.append(self.body[j][i])
      arr.append(row)
    return Matrix(arr)
  
  def getDeterminante(self):
    pass