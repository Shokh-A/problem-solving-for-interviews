

# Problem:
# Partition: Write code to partition a linked list around a value x, such that all nodes less than x come
# before all nodes greater than or equal to x. If x is contained within the list, the values of x only need
# to be after the elements less than x (see below). The partition element x can appear anywhere in the
# "right partition"; it does not need to appear between the left and right partitions.
# EXAMPLE:
# Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition= 5]
# Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8

# Brainstorming:
# We have to collect all the nodes with value less than given partition on the left. 
# 

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
  def partition(self, node: ListNode, x: int):
    left = ListNode(val=0, next=None)
    left_head = left
    right = ListNode(val=0, next=None)
    right_head = right
    while node != None:
      if node.val < x:
        left.next = node
        left = left.next
      else:
        right.next = node
        right = right.next
      node = node.next

    right.next = None
    left.next = right_head.next

    return left_head.next
  
  def partition1(self, node: ListNode, x: int) -> ListNode:
    head = node
    tail = node

    while node != None:
      next = node.next
      if node.val < x:
        node.next = head
        head = node
      else:
        tail.next = node
        tail = node
      node = next
    
    tail.next = None

    return head

# Test
sol = Solution()
# Test case 1
l = ListNode(val=3, next=
    ListNode(val=5, next=
    ListNode(val=8, next=
    ListNode(val=5, next=
    ListNode(val=10, next=
    ListNode(val=2, next=
    ListNode(val=1, next=None)))))))

print("1st test case", sol.partition1(l, x=5))
# Test case 2
# print("2nd test case", sol.func())
# Test case 3
# print("3rd test case", sol.func())
