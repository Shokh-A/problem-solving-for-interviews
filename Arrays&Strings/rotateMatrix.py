from typing import List

# Problem:
# Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
# bytes, write a method to rotate the image by 90 degrees. Can you do this in place?

# Brainstorming:
# Matrix is of NxN size
# Store one layer when changing the one next to it
# edge to edge changes are applied


class Solution:

  # Time - O(n^2), since we have to go through each element
  def rotateMatrix90(self, matrix: List[List]) -> List[List]:
    n = len(matrix)

    for layer in range(n // 2):
      first = layer
      last = n - 1 - layer
      for i in range(first, last):
        offset = i - first
        top = matrix[first][i]

        # left -> top
        matrix[first][i] = matrix[last-offset][first]
        
        # bottom -> left
        matrix[last-offset][first] = matrix[last][last-offset]
        
        # right -> bottom
        matrix[last][last-offset] = matrix[i][last]
        
        # top -> right
        matrix[i][last] = top # right <- saved top
        

    return matrix
  
# Test
sol = Solution()
# Test case 1
m = [[1,2,3],
     [4,5,6],
     [7,8,9]]
print("1st test case:", sol.rotateMatrix90(m))
# Test case 2
m = [[7,4,1],
     [8,5,2],
     [9,6,3]]
print("2nd test case:", sol.rotateMatrix90(m))
# Test case 3
m = [[9,8,7],
     [6,5,4],
     [3,2,1]]
print("3rd test case:", sol.rotateMatrix90(m))
# Test case 4
m = [[3,6,9],
     [2,5,8],
     [1,4,7]]
print("4th test case:", sol.rotateMatrix90(m))