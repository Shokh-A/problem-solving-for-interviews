# Problem:
# Check Subtree: T1 and T2 are two very large binary trees, with T1 much bigger than T2.
# Create an algorithm to determine if T2 is a subtree of T1. A tree T2 is a subtree of 
# T1 if there exists a node n in T1 such that the subtree of n is identical to T2. That 
# is, if you cut off the tree at node n, the two trees would be identical.

# Brainstorming:
#

from tree import TreeNode

class Solution:

  def contains_tree(self, node1: TreeNode, node2: TreeNode):
    if not node2: return True
    return self.subtree(node1, node2)
  
  def subtree(self, node1: TreeNode, node2: TreeNode):
    if not node1: return False
    elif node1.val == node2.val and self.matchTree(node1, node2):
      return True
    return self.subtree(node1.left, node2) or self.subtree(node1.right, node2)
  
  def matchTree(self, node1: TreeNode, node2: TreeNode):
    if not node1 and not node2: return True
    elif not node1 or not node2: return False
    elif node1.val != node2.val: return False
    else: return self.matchTree(node1.left, node2.left) and self.matchTree(node1.right, node2.right)

# Test
sol = Solution()
# Test case 1
node1 = TreeNode(val=1)
node1.left = TreeNode(val=2)
node1.right = TreeNode(val=3)
node1.left.left = TreeNode(val=4)
node1.left.right = TreeNode(val=5)
node1.right.left = TreeNode(val=6)
node1.right.right = TreeNode(val=7)

node2 = TreeNode(val=3)
node2.left = TreeNode(val=6)
node2.right = TreeNode(val=7)
print("1st test case", sol.contains_tree(node1, node2))
