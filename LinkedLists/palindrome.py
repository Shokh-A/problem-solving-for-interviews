

# Problem:
# Palindrome: Implement a function to check if a linked list is a palindrome.

# Brainstorming:
# Reverse and compare.

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

  def reverse(self, node: ListNode) -> ListNode:
    reversed = None
    while node != None:
      n = ListNode(val=node.val, next=None)
      n.next = reversed
      reversed = n
      node = node.next
    return reversed

  def isPalindrome(self, node: ListNode) -> bool:
    reversed = self.reverse(node)
    while reversed != None and node != None:
      if reversed.val != node.val:
        return False
      reversed = reversed.next
      node = node.next

    return reversed == None and node == None
  
  def isPalindrome_iterative(self, node: ListNode) -> bool:
    stack = []
    fast = node
    slow = node
    while fast != None and fast.next != None:
      stack.append(slow.val)
      slow = slow.next
      fast = fast.next.next

    if fast != None:
      slow = slow.next

    while slow != None:
      if slow.val != stack.pop():
        return False
      slow = slow.next

    return True
  
  # Recursive
  def isPalindrome_recursive(self, node: ListNode) -> bool:
    size = self.length(node)
    return self.isPalindromeRecurse(node, size)
  
  def isPalindromeRecurse(self, node: ListNode, length: int):
    if node == None or length <= 0:
      return node, True
    elif length == 1:
      return node.next, True
    
    res = self.isPalindromeRecurse(node.next, length - 2)

    if not res[1] or res[0] == None:
      return res
    
    res = (res[0].next, res[0].val == node.val)

    return res

  def length(self, node: ListNode) -> int:
    size = 0
    while node != None:
      size += 1
      node = node.next
    return size

# Test
sol = Solution()
# Test case 1
l = ListNode(val=0, next=
    ListNode(val=1, next=
    ListNode(val=2, next=
    ListNode(val=3, next=
    ListNode(val=2, next=
    ListNode(val=1, next=
    ListNode(val=0, next=None)))))))
print("1st test case", sol.isPalindrome_recursive(l))
# Test case 2
# print("2nd test case", sol.func())
# Test case 3
# print("3rd test case", sol.func())
