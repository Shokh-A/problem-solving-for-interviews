# Problem:
# Random Node: You are implementing a binary search tree class from scratch, 
# which, in addition to insert, find, and delete, has a method getRandomNode() 
# which returns a random node from the tree. All nodes should be equally likely
# to be chosen. Design and implement an algorithm for getRandomNode, and explain 
# how you would implement the rest of the methods.

# Brainstorming:
# Indexing each node and choosing random index works, but it is slow since on add/delete
# indexes should be updated.

import random

class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
    self.size = 1

  # Time - O(NlogN) in balanced tree or O(D), where D is the max depth of the tree
  def getRandomNode(self):
    leftSize = 0 if not self.left else self.left.size
    index = random.randint(0, self.size-1)
    if index < leftSize:
      return self.left.getRandomNode()
    elif index == leftSize:
      return self
    else:
      return self.right.getRandomNode()
    
  def insertInOrder(self, val: int):
    if val < self.val:
      if not self.left:
        self.left = TreeNode(val=val)
      else:
        self.left.insertInOrder(val)
    else:
      if not self.right:
        self.right = TreeNode(val=val)
      else:
        self.right.insertInOrder(val=val)
    self.size += 1

  def __str__(self):
    return str(self.val)
    

# Test
# sol = Solution()
# Test case 1
node = TreeNode(val=20)
node.insertInOrder(10)
node.insertInOrder(30)
node.insertInOrder(5)
node.insertInOrder(15)
node.insertInOrder(35)
node.insertInOrder(3)
node.insertInOrder(7)
node.insertInOrder(17)
print("1st test case", node.getRandomNode())
