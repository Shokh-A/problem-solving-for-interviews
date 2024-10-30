# Problem:
# First Common Ancestor: Design an algorithm and write code to find the first common ancestor 
# of two nodes in a binary tree. Avoid storing additional nodes in a data structure.
# NOTE: This is not necessarily a binary search tree.

# Brainstorming:
# Does the tree node contain pointer to its parent?

from tree import TreeNode

class Solution:
  # Let's assume a node has link to its parent
  # Time - O(d), where d is the depth of deeper node.
  def firstCommonAncestor(self, node1: TreeNode, node2: TreeNode):
    delta = self.depth(node1) - self.depth(node2)
    first = node2 if delta > 0 else node1
    second = node1 if delta > 0 else node2
    second = self.goUpBy(second, abs(delta))

    while first != second and first and second:
      first = first.parent
      second = second.parent

    return None if first == None or second == None else first
  
  def goUpBy(self, node: TreeNode, delta: int):
    while (delta > 0 and node):
      node = node.parent
      delta -= 1
    return node

  def depth(self, node: TreeNode):
    depth = 0
    while node:
      node = node.parent
      depth += 1
    return depth
  

  # Second solution with better worst-case runtime
  # Time - O(t), where t is the size of the subtree for the first common ancestor.
  # In the worst case, this will be O(n), where n is the number of nodes in the tree.
  def commonAncestor(self, root: TreeNode, node1: TreeNode, node2: TreeNode):
    if (not self.covers(root, node1) or not self.covers(root, node2)):
      return None
    elif (self.covers(node1, node2)):
      return node1
    elif (self.covers(node2, node1)):
      return node2
    
    sibling = self.getSibling(node1)
    parent = node1.parent
    while not self.covers(sibling, node2):
      parent = parent.parent

    return parent

  def covers(self, root: TreeNode, node: TreeNode):
    if (root == None): return False
    if (root == node): return True
    return self.covers(root.left, node) or self.covers(root.right, node)

  def getSibling(self, node: TreeNode):
    if (node == None or node.parent == None):
      return None
    
    parent = node.parent
    return parent.right if parent.left == node else parent.left
  
  # Third solution (node does not have parent link)
  # Time - O(n) on balanced tree.
  def commonAncestor3(self, root: TreeNode, node1: TreeNode, node2: TreeNode):
    if (not self.covers(root, node1) or not self.covers(root, node2)):
      return None
    
    return self.ancestorHelper(root, node1, node2)
  
  def ancestorHelper(self, root: TreeNode, node1: TreeNode, node2: TreeNode):
    if (not root or root == node1 or root == node2):
      return root
    
    node1IsOnLeft = self.covers(root.left, node1)
    node2IsOnLeft = self.covers(root.left, node2)
    if (node1IsOnLeft != node2IsOnLeft):
      return root
    
    childSide = root.left if node1IsOnLeft else root.right
    return self.ancestorHelper(childSide, node1, node2)


  # Fourth solution (node does not have link to parent - optimized)
  # In case on of the nodes does not belong in the tree.
  def commonAncestor4(self, root: TreeNode, node1: TreeNode, node2: TreeNode):
    (node, isAncestor) = self.commonAncestorHelper(root, node1, node2)
    if (isAncestor):
      return node
    return None

  def commonAncestorHelper(self, root: TreeNode, node1: TreeNode, node2: TreeNode):
    if not root: return (None, False)

    if root == node1 and root == node2:
      return (root, True)
    
    (nodeX, isAncestorX) = self.commonAncestorHelper(root.left, node1, node2)
    if (isAncestorX):
      return (nodeX, isAncestorX)
    
    (nodeY, isAncestorY) = self.commonAncestorHelper(root.right, node1, node2)
    if (isAncestorY):
      return (nodeY, isAncestorY)
    
    if (nodeX and nodeY):
      return (root, True)
    elif (root == node1 or root == node2):
      isAncestor = nodeX or nodeY
      return (root, isAncestor)
    else:
      return (nodeX if nodeX else nodeY, False)

# Test
sol = Solution()
# Test case 1
root = TreeNode(1)
root.left = TreeNode(2, parent=root)
root.right = TreeNode(3, parent=root)
node1 = TreeNode(4, parent=root.left)
root.left.left = node1
node2 = TreeNode(5, parent=root.left)
root.left.right = node2
root.right.left = TreeNode(6, parent=root.right)
root.right.right = TreeNode(7, parent=root.right)

randomNode = TreeNode(6)
print("1st test case", sol.commonAncestor4(root, node1, node2))