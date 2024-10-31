# Problem:
# BST Sequences: A binary search tree was created by traversing through an array from left to right
# and inserting each element. Given a binary search tree with distinct elements, print all possible
# arrays that could have led to this tree.
# EXAMPLE
# Input: 2 -> L: 1, R: 3
# Output: {2, 1, 3}, {2, 3, 1}

# Brainstorming:
# BST contains only distint elements.

from tree import TreeNode

class Solution:

  def allSequences(self, root: TreeNode):
    if not root: return []
    return self.helper(root)
  
  def helper(self, node: TreeNode):
    if not node: return [[]]

    right_sequences = self.helper(node.right)
    left_sequences = self.helper(node.left)
    sequences = []
    for right in right_sequences:
      for left in left_sequences:
        sequences = self.weave(left, right, [node.val], sequences)

    return sequences
  
  def weave(self, first, second, prefix, results):
    if len(first) == 0 or len(second) == 0:
      result = prefix.copy()
      result.extend(first)
      result.extend(second)
      results.append(result)
      return results
    
    head = first[0]
    prefix.append(head)
    results = self.weave(first[1:], second, prefix, results)
    prefix.pop()
    head = second[0]
    prefix.append(head)
    results = self.weave(first, second[1:], prefix, results)
    prefix.pop()
    return results

  def find_bst_sequences_backtracking(self, root:TreeNode):
    if not root:
        return []

    ret_backtracking = []

    def backtracking(choices, weave):
        if not len(choices):
            ret_backtracking.append(weave)
            return

        for i in range(len(choices)):
            nextchoices = choices[:i] + choices[i + 1 :]
            if choices[i].left:
                nextchoices += [choices[i].left]
            if choices[i].right:
                nextchoices += [choices[i].right]
            backtracking(nextchoices, weave + [choices[i].val])

    backtracking([root], [])
    return ret_backtracking

# Test
sol = Solution()
# Test case 1
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(8)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
# root.right.left = TreeNode(6)
# root.right.right = TreeNode(9)
print("1st test case", sol.find_bst_sequences_backtracking(root))