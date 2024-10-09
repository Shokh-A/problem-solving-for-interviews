# Problem:
# Remove Dups: Write code to remove duplicates from an unsorted linked list.
# FOLLOW UP
# How would you solve this problem if a temporary buffer is not allowed?

# Brainstorming:
# Is the linked list doubly or singly linked?
# Keep in mind that it is unsorted linked list.
# In case of follow up solution, the time complexity increases.

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
  def removeDups(self, node: ListNode) -> ListNode:
    seen = set()
    head = node
    prev = None
    while node != None:
      if node.val in seen:
        prev.next = node.next
      else:
        prev = node
        seen.add(node.val)
      node = node.next
    return head
  
  # FOLLOW UP - NO BUFFER ALLOWED
  # Time - O(n^2)
  # Space - O(1)
  def removeDupsFollowUp(self, node: ListNode) -> ListNode:
    head = node
    while node != None:
      cur = node.next
      prev = node
      while cur != None:
        if cur.val == node.val:
          prev.next = cur.next
        else:
          prev = cur
        cur = cur.next
      node = node.next

    return head

# Test
sol = Solution()
# Test case 1
l = ListNode(val=2, next=
    ListNode(val=1, next=
    ListNode(val=2, next=
    ListNode(val=1, next=
    ListNode(val=3, next=
    ListNode(val=1, next=None))))))
print("1st test case:", sol.removeDupsFollowUp(l))
# Test case 2
l = ListNode(val=2, next=ListNode(val=2, next=None))
print("2nd test case:", sol.removeDupsFollowUp(l))
