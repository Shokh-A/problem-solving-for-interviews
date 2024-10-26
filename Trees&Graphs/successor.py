# Problem:
# Successor: Write an algorithm to find the "next" node (i.e., in-order successor)
# of a given node in a binary search tree. You may assume that each node has a link
# to its parent.

# Brainstorming:
# The input can be any node of the tree, it is vital to understand that before trying
# to solve the problem.

class TreeNode:
  def __init__(self, val, left=None, right=None, parent=None):
    self.val = val
    self.left = left
    self.right = right
    self.parent = parent

  def __str__(self):
    return str(self.val)

class Solution:
  def inorderSucc(self, node: TreeNode):
    if not node: return

    if node.right:
      return self.leftMostChild(node.right)
    else:
      q = node
      x = q.parent
      while x and x.left != q:
        q = x
        x = x.parent
    return x
  
  def leftMostChild(self, node: TreeNode):
    if not node: return
    while node.left:
      node = node.left
    return node

# Test
sol = Solution()
# Test case 1
root = TreeNode(5)
root.left = TreeNode(3, parent=root)
root.right = TreeNode(8, parent=root)
root.left.left = TreeNode(2, parent=root.left)
node = TreeNode(4, parent=root.left)
root.left.right = node
root.right.left = TreeNode(6, parent=root.right)
root.right.right = TreeNode(9, parent=root.right)
print("1st test case", sol.inorderSucc(node))

