# Problem:
# Check Balanced: Implement a function to check if a binary tree is balanced.
# For the purposes of this question, a balanced tree is defined to be a tree
# such that the heights of the two subtrees of any node never differ by more
# than one.

# Brainstorming:
# Get the height at each subtree and compare them, if different - return false,
# else true. - Not very effective.
# Another solution is to 

from tree import TreeNode

class Solution:

  def getHeight(self, root: TreeNode):
    if not root: return -1
    return max(self.getHeight(root.left), self.getHeight(root.right)) + 1

  # Time - O(nlogn)
  def isBalanced_a(self, root: TreeNode):
    if not root: return True

    heightDiff = abs(self.getHeight(root.left) - self.getHeight(root.right))
    if heightDiff > 1:
      return False
    else:
      return self.isBalanced_a(root.left) and self.isBalanced_a(root.right)

  # Time - O(n)
  # Space - O(h), where h - the height of the tree
  def isBalanced(self, root: TreeNode):
    if not root: return 0, True
    left, balanced = self.isBalanced(root.left)
    if not balanced: return 1 + left, False
    right, balanced = self.isBalanced(root.right)
    if not balanced: return 1 + right, False
    height = 1 + max(left, right)
    if abs(right-left) > 1 or not balanced:
      return height, False
    return height, True

# Test
sol = Solution()
# Test case 1
root = TreeNode(0)
root.left = TreeNode(1)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(5)
root.right.right = TreeNode(6)
root.left.left.left = TreeNode(7)
# root.left.left.left.left = TreeNode(8)
print("1st test case", sol.isBalanced(root))