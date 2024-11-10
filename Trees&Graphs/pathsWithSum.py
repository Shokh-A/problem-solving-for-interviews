# Problem:
# Paths with Sum: You are given a binary tree in which each node contains an integer value
# (which might be positive or negative). Design an algorithm to count the number of paths 
# that sum to a given value. The path does not need to start or end at the root or a leaf,
# but it must go downwards (traveling only from parent nodes to child nodes).

# Brainstorming:
# It is important to remember to that start and end of path go downwards, but not neccessarily
# from root to leaf.

from tree import TreeNode

class Solution:

  # Brute force
  # Time - O(nlogn)
  def countPathsWithSum(self, root: TreeNode, targetSum: int):
    if not root: return 0

    pathsFromRoot = self.countPathsFromNode(root, targetSum, 0)

    pathsOnLeft = self.countPathsWithSum(root.left, targetSum)
    pathsOnRight = self.countPathsWithSum(root.right, targetSum)

    return pathsFromRoot + pathsOnLeft + pathsOnRight
  
  def countPathsFromNode(self, node: TreeNode, targetSum: int, currentSum: int):
    if not node: return 0

    currentSum += node.val

    totalPaths = 0
    if currentSum == targetSum:
      totalPaths += 1

    totalPaths += self.countPathsFromNode(node.left, targetSum, currentSum)
    totalPaths += self.countPathsFromNode(node.right, targetSum, currentSum)
    return totalPaths
  
  # Optimized
  # Time - O(n)
  def countPaths(self, root: TreeNode, targetSum: int):
    return self.countPathsHelper(root, targetSum, 0,  dict())


  def countPathsHelper(self, node: TreeNode, targetSum: int, runningSum: int, pathCount: dict):
    if not node: return 0

    runningSum += node.val
    s = runningSum - targetSum
    totalPaths = pathCount.get(s, 0)

    if runningSum == targetSum:
      totalPaths += 1

    self.incrementHashTable(pathCount, runningSum, 1)
    totalPaths += self.countPathsHelper(node.left, targetSum, runningSum, pathCount)
    totalPaths += self.countPathsHelper(node.right, targetSum, runningSum, pathCount)
    self.incrementHashTable(pathCount, runningSum, -1)

    return totalPaths
  
  def incrementHashTable(self, hashTable: dict, key: int, delta: int):
    newCount = hashTable.get(key, 0) + delta
    if newCount == 0:
      hashTable.pop(key)
    else:
      hashTable.setdefault(key, newCount)

# Test
sol = Solution()
# Test case 1
root = TreeNode(val=10)
root.left = TreeNode(val=5)
root.right = TreeNode(val=-3)
root.left.left = TreeNode(val=3)
root.left.right = TreeNode(val=2)
root.right.right = TreeNode(val=11)
root.left.left.left = TreeNode(val=3)
root.left.left.right = TreeNode(val=-2)
root.left.right.right = TreeNode(val=1)
print("1st test case", sol.countPaths(root, 8))