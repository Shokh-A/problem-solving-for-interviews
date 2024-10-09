
# Problem:
# Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.

# Brainstorming:
# The list is singly linked
# While traversing through the list we can store the index of the nodes and at the end calculate the relative
# position to last. In this case, space complexity would be O(n), Time - O(n)

# Another solution would be to traverse and find the last node and its index. Then traverse the node again and 
# stop at Kth node. 

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

  def __str__(self):
    s = ""
    while self != None:
      s += str(self.val) + " -> "
      self = self.next
    s += "None"
    return s
  
class Solution:

  # Time - O(n)
  # Space - O(n)
  def kThElementToLast(self, node: ListNode, k: int) -> ListNode:
    if k < 0: return None
    index_map = dict()
    i = 0
    while node != None:
      index_map[i] = node
      node = node.next
      i += 1
    
    return index_map[i-1-k] if i - 1 - k in index_map.keys() else None
  
  # Time - O(n^2)
  # Space - O(1)
  def kThElementToLast_optimal_space(self, node: ListNode, k: int) -> ListNode:
    if k < 0: return None
    
    head = node
    last = 0

    while node.next != None:
      node = node.next
      last += 1
    
    node = head
    while node != None and last != k:
      node = node.next
      last -= 1

    return node
  
  # In case we do not have to return the element
  def printKth(self, node: ListNode, k: int):
    if node == None: return 0
    index = self.printKth(node.next, k) + 1
    if index == k: print(str(k) + "th to last node is " + str(node.val))
    return index
  
  # Optimal solution by space and time
  # Time - O(n)
  # Space - O(1)
  def getKth_optimal(self, node: ListNode, k: int) -> ListNode:
    if k < 0: return None
    p1 = node
    p2 = node
    i = 0
    while i < k:
      if p1 == None: return None
      p1 = p1.next
      i += 1

    while p1 != None:
      p1 = p1.next
      p2 = p2.next

    return p2

  
# Test
sol = Solution()
# Test case 1
l = ListNode(val=97, next=
    ListNode(val=100, next=
    ListNode(val=3, next=
    ListNode(val=17, next=
    ListNode(val=20, next=None)))))
print("negative K test case:", sol.getKth_optimal(l, -1))
print("0th test case:", sol.getKth_optimal(l, 0))
print("1st test case:", sol.getKth_optimal(l, 1))
print("2nd test case:", sol.getKth_optimal(l, 2))
print("3rd test case:", sol.getKth_optimal(l, 3))
print("4th test case:", sol.getKth_optimal(l, 4))
print("5th test case:", sol.getKth_optimal(l, 5))