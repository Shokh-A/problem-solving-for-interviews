# Problem:
# Route Between Nodes: Given a directed graph, design an algorithm
# to find out whether there is a route between two nodes.

# Brainstorming:
# In tasks with graphs dfs and bfs are very common.
# Keep in mind that this is directed graph.
# Solution to this problem is to simply start bfs or dfs from one
# given node until second node is found.

from collections import deque
from typing import List

class Node:
  def __init__(self, val, children = []):
    self.val = val
    self.children = children

class Graph:
  def __init__(self, nodes=[]):
    self.nodes = nodes

class Solution:
  def doesRouteExist(self, graph: Graph, node1: Node, node2: Node):
    visited = set()
    q = deque([node1])
    while len(q) != 0:
      node = q.popleft()
      if node == node2:
        return True
      for child in node.children:
        if child not in visited:
          q.append(child)

    return False

# Test
sol = Solution()
# Test case 1
n1 = Node(val=1, children=[])
n2 = Node(val=2, children=[n1])
n3 = Node(val=3, children=[n1])
n4 = Node(val=4, children=[n2, n3])
n5 = Node(val=5, children=[n3, n4])
n6 = Node(val=6, children=[n3, n5])
g = Graph(nodes=[n1,n2,n3,n4,n5,n6])
print("1st test case", sol.doesRouteExist(g, n6, n2))
