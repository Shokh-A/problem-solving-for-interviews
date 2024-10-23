# Problem:
# List of Depths: Given a binary tree, design an algorithm which creates a linked list of all 
# the nodes at each depth (e.g., if you have a tree with depth D, you'll have D linked lists).

# Brainstorming:
#

from tree import TreeNode
from linkedList import LinkedList
from collections import deque

class Solution:
  def create_node_list_by_depth(self, tree_root):
    # BFS.
    levels = {}
    q = deque()
    q.append((tree_root, 0))

    while len(q) > 0:
        node, level = q.popleft()
        if level not in levels:
            # First node in the level
            levels[level] = LinkedList()
        # Nodes already exist
        levels[level].add(node)

        # Push onto queue
        if node.left:
            q.append((node.left, level + 1))
        if node.right:
            q.append((node.right, level + 1))
    return levels

  def create_node_list_by_depth_b(self, tree):
    if not tree:
        return []

    curr = tree
    result = [LinkedList([curr])]
    level = 0

    while result[level]:
        result.append(LinkedList())
        for linked_list_node in result[level]:
            n = linked_list_node.value
            if n.left:
                result[level + 1].add(n.left)
            if n.right:
                result[level + 1].add(n.right)
        level += 1
    return result

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
# for level in sol.create_node_list_by_depth_b(root):
#   print(level)
print("1st test case", sol.create_node_list_by_depth_b(root))
