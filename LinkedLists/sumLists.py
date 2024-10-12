

# Problem:
# Sum Lists: You have two numbers represented by a linked list, where each node contains a single
# digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list.
# Write a function that adds the two numbers and returns the sum as a linked list.
# EXAMPLE:
# Input: (7 -> 1 -> 6) + (5 -> 9 -> 2).That is, 617 + 295.
# Output: 2 -> 1 -> 9. That is, 912.
# FOLLOW UP:
# Suppose the digits are stored in forward order. Repeat the above problem.
# Input: (6 -> 1 -> 7) + (2 -> 9 -> 5).That is,617 + 295.
# Output: 9 -> 1 -> 2. That is, 912.

# Brainstorming:
# Keep in mind that the length of the lists can be different.
# If the sum of two digits is greater or equal to 10 one additional node may be needed.
# In summation we start from the right digit, so these lists are perfect for this occasion
# as they are reversed.
# Returned list should keep the order and stay reversed.
# For the follow up question we can reverse the given lists and then perform summation above,
# and then reverse the list again.

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

  # Time - O(n), where n is the length of the longer list.
  # Space - O(n), we are creating new linked list
  def sumLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    s = ListNode(val=0, next=None)
    s_head = s

    extra = 0
    while l1 != None and l2 != None:
      s.next = ListNode(val=(l1.val + l2.val + extra) % 10, next=None)
      extra = (l1.val + l2.val + extra) // 10
      s = s.next
      l1 = l1.next
      l2 = l2.next

    while l1 != None:
      s.next = ListNode(val=(l1.val + extra) % 10, next=None)
      extra = (l1.val + extra) // 10
      s = s.next
      l1 = l1.next

    while l2 != None:
      s.next = ListNode(val=(l2.val + extra) % 10, next=None)
      extra = (l2.val + extra) // 10
      s = s.next
      l2 = l2.next

    return s_head.next
  
  # Recursive
  def sumLists_recursive(self, l1: ListNode, l2: ListNode, carry: int) -> ListNode:
    if l1 == None and l2 == None and carry == 0:
      return None

    result = ListNode()
    value = carry
    if l1 != None:
      value += l1.val
    
    if l2 != None:
      value += l2.val

    result.val = value % 10

    if l1 != None or l2 != None:
      more = self.sumLists_recursive(None if l1 == None else l1.next,
                                     None if l2 == None else l2.next,
                                     1 if value >= 10 else 0)
      result.next = more

    return result
  
  # One way to solve this would be to reverse lists and perform the above function on the 
  # reversed lists, and then reverse the result again.
  # The other possible solution would be to build numbers from digits and do summation on
  # numbers and the build Linked list from the result.
  def sumLists_followUp(self, l1: ListNode, l2: ListNode) -> ListNode:

    n1 = 0
    n2 = 0
    while l1 != None:
      n1 = (n1 * 10) + l1.val
      l1 = l1.next

    while l2 != None:
      n2 = (n2 * 10) + l2.val
      l2 = l2.next

    s = n1 + n2
    res = ListNode(val=0, next=None)
    head = res
    for digit in str(s):
      res.next = ListNode(val=(int(digit)), next=None)
      res = res.next

    return head.next


# Test
sol = Solution()
# Test case 1
l1 = ListNode(val=7, next=
     ListNode(val=1, next=
     ListNode(val=6, next=None)))
l2 = ListNode(val=5, next=
     ListNode(val=9, next=
     ListNode(val=2, next=None)))
print("1st test case", sol.sumLists_recursive(l1, l2, 0))
# Test case 2
l1 = ListNode(val=7, next=
     ListNode(val=1, next=None))
l2 = ListNode(val=5, next=
     ListNode(val=9, next=
     ListNode(val=2, next=None)))
# print("2nd test case", sol.sumLists_followUp(l1, l2))
# Test case 3
l1 = ListNode(val=7, next=None)
l2 = ListNode(val=5, next=
     ListNode(val=9, next=
     ListNode(val=2, next=None)))
# print("3rd test case", sol.sumLists_followUp(l1, l2))
