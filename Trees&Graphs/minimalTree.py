# Problem:
# Minimal Tree: Given a sorted (increasing order) array with unique 
# integer elements, write an algorithm to create a binary search 
# tree with minimal height.

# Brainstorming:
# Considering the given array is sorted, splitting it in the middle
# will give us the most effective root val, then we can recursively repeat
# this for the split sections until we have built binary search tree.

class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

  def disp(self, nesting=0):
    indent = " " * nesting * 2
    output = f"{self.val}\n"
    if self.left is not None:
      output += f"{indent}L:"
      output += self.left.disp(nesting + 1)
    if self.right is not None:
      output += f"{indent}R:"
      output += self.right.disp(nesting + 1)
    return output

  def __str__(self):
    return self.disp()

  # def __str__(self):
  #   s = ""
  #   s += "(val: " + str(self.val)
  #   s += ", left -> " + (str(self.left) if self.left else "None")
  #   s += ", right -> " + (str(self.right) if self.right else "None")
  #   s += ")"
  #   return s


class Solution:
  def createBinarySearchTree(self, arr):
    if not arr: return None
    midIndex = len(arr) // 2
    root = TreeNode(val=arr[midIndex])
    root.left = self.createBinarySearchTree(arr[:midIndex])
    root.right = self.createBinarySearchTree(arr[midIndex + 1:])

    return root

# Test
sol = Solution()
# Test case 1
print("1st test case:\n", sol.createBinarySearchTree([1,2,3,4,5,6,7,8,9]))

