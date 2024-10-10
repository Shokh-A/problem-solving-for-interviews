

# Problem:
# Delete Middle Node: Implement an algorithm to delete a node in the middle
# (i.e., any node but the first and last node, not necessarily the exact middle)
# of a singly linked list, given only access to that node.
# EXAMPLE:
# lnput: the node c from the linked list a->b->c->d->e->f
# Result: nothing is returned, but the new linked list looks like a->b->d->e->f

# Brainstorming:
# Since we are given middle node as input and we have only singly linked list,
# we cannot change the pointer of the node before given node to next after given node.
# So we have to update values of the nodes starting from given one to the next node's value.

# In case given node is the last node, the problem can not be solved, but the node value can
# still be changed to indicate it is supposed to be deleted. (Tell interviewer about this)

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
  # Space - O(1)
  # Unneccesarily complicated solution.
  def deleteMiddleNode(self, node: ListNode):
    while node.next != None:
      node.val = node.next.val
      if node.next.next == None:
        node.next = None
        break
      node = node.next

  # Time - O(1)
  # Space - O(1)
  def deleteMiddleNode1(self, node: ListNode):
    if node == None or node.next == None: return
    next = node.next
    node.val = next.val
    node.next = next.next

# Test
sol = Solution()
# Test case 1
mid = ListNode(val=3, next=
      ListNode(val=4, next=
      ListNode(val=5, next=
      ListNode(val=6, next=None))))
l = ListNode(val=1, next=
    ListNode(val=2, next=mid))
sol.deleteMiddleNode1(mid)
print("1st test case", l)
# Test case 2
# print("2nd test case", sol.deleteMiddleNode(l))
# Test case 3
# print("3rd test case", sol.deleteMiddleNode(l))
