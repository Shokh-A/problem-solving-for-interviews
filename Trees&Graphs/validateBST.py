# Problem:
# Validate BST: Implement a function to check if a binary tree is a binary search tree.

# Brainstorming:
# Can the tree contain duplicates? Shall we store the duplicates to the left or right?
# In BST, all elements in the left subtree should be less or equal, on the right - greater.

from tree import TreeNode

class Solution:

  # If there are no duplications allowed in the tree we can convert the tree into array
  # and compare adjacent elements.
  def isBST(self, root: TreeNode):
    arr = self.treeToArray(root)
    for i in range(1, len(arr)):
      if arr[i] <= arr[i-1]: return False
    return True

  def treeToArray(self, root: TreeNode):
    result = []
    def in_order_traversal(node: TreeNode):
      if not node: return
      in_order_traversal(node.left)
      result.append(node.val)
      in_order_traversal(node.right)
    
    in_order_traversal(root)
    return result

  # Recursive solution, duplications in the tree are permittable. 
  def isBST_recursive(self, root: TreeNode, min_val = None, max_val = None):
    if not root: return True
    if (min_val and root.val < min_val) or (max_val and root.val >= max_val):
      return False
    return self.isBST_recursive(root.left, min_val, root.val) and self.isBST_recursive(root.right, root.val, max_val)

# Test
sol = Solution()
# Test case 1
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(8)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)
# root.left.left.left = TreeNode(7)
print("1st test case", sol.isBST_recursive(root))

