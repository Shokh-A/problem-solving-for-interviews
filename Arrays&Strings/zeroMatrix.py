from typing import List

# Problem:
# Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, 
# its entire row and column are set to 0.

# Brainstorming:
# matrix is of MxN size, keep that in mind.
# do not repeat setting whole row and column operation if row and column are already set to 0
# we could store rows and columns that are already changed and skip them
# if there are two 0 zeros in the row or column it should still change the row or column they belong too separately.

class Solution:

  # Time - too slow unneccessary iterations.
  # Space - storing indexes is overkills storing rows and columns is enough
  def zeroMatrix(self, matrix: List[List]) -> List[List]:
    mem = []

    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
      for j in range(m):
        if matrix[i][j] == 0 and (i, j) not in mem:
          self.zeroRowAndCol(mem, matrix, i, j, n, m)

    return matrix


  def zeroRowAndCol(self, mem: List, matrix, i, j, n, m):
    mem.append((i, j))
    
    # Change i-th row to 0
    for k in range(m):
      if self.isChanged(i, k, mem, matrix):
        self.zeroRowAndCol(mem, matrix, i, k, n, m)
      matrix[i][k] = 0
      mem.append((i, k))

    # Change j-th col to 0
    for k in range(n):
      if self.isChanged(k, j, mem, matrix):
        self.zeroRowAndCol(mem, matrix, k, j, n, m)
      matrix[k][j] = 0
      mem.append((k, j))

  def isChanged(self, i, j, mem, matrix):
    return matrix[i][j] == 0 and (i, j) not in mem



  # Optimal solution:
  # Time - O(mn)
  # Space - O(n)
  def setZeros(self, matrix: List[List]) -> List[List]:
    row = [False for _ in range(len(matrix))]
    column = [False for _ in range(len(matrix[0]))]

    for i in range(len(matrix)):
      for j in range(len(matrix[0])):
        if matrix[i][j] == 0:
          row[i] = True
          column[i] = True

    for i in range(len(row)):
      if (row[i]): self.nulifyRow(matrix, i)

    for j in range(len(column)):
      if (column[j]): self.nulifyRow(matrix, j)

    return m

  def nulifyRow(self, matrix, row):
    for j in range(len(matrix[0])):
      matrix[row][j] = 0

  def nulifyColumn(self, matrix, col):
    for i in range(len(matrix)):
      matrix[i][col] = 0


  # Solution with O(1) space complexity
  def setZeros_1(self, matrix: List[List]) -> List[List]:
    rowHasZero = False
    colHasZero = False

    m = len(matrix)
    n = len(matrix[0])
    for j in range(n):
      if matrix[0][j] == 0:
        rowHasZero = True
        break

    for i in range(m):
      if matrix[i][0] == 0:
        colHasZero = True
        break

    for i in range(1, m):
      for j in range(1, n):
        if matrix[i][j] == 0:
          matrix[0][j] = 0
          matrix[i][0] = 0

    for i in range(1, m):
      if (matrix[i][0] == 0): self.nulifyRow(matrix, i)

    for j in range(1, n):
      if (matrix[0][j] == 0): self.nulifyColumn(matrix, j)

    if rowHasZero:
      self.nulifyRow(matrix, 0)
    
    if colHasZero:
      self.nulifyColumn(matrix, 0)

    return matrix
    

      
# Test
sol = Solution()
# Test case 1
m = [[1,2,0,4],
     [1,2,3,4],
     [1,2,0,4],
     [1,2,3,4],]
print("1st test case:", sol.setZeros_1(m))

    

