

# Problem:
# Loop Detection: Given a circular linked list, implement an algorithm that returns 
# the node at the beginning of the loop.
# DEFINITION
# Circular linked list: A (corrupt) linked list in which a node's next pointer points
# to an earlier node, so as to make a loop in the linked list.
# EXAMPLE:
# Input: A - > B - > C - > D - > E - > C [the same C as earlier]
# Output: C

# Brainstorming:
# We can store the nodes in hashtable and if the node is seen that would be the head of
# the loop.


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
  # Spce - O(n)
  def getLoopHead(self, node: ListNode):
    seen = set() 
    cur = node
    while cur is not None:
        if cur in seen: 
            return cur 
        seen.add(cur)
        cur = cur.next
    return None 
  
  def getLoopHead_two_pointers(self, node: ListNode) -> ListNode:
    slow = node
    fast = node

    while fast != None and fast.next != None:
      slow = slow.next
      fast = fast.next.next
      if slow == fast:
        break
    
    if fast == None or fast.next == None:
      return None
    
    slow = node
    while slow != fast:
      slow = slow.next
      fast = fast.next

    return fast

# Test
sol = Solution()
# Test case 1
node1 = ListNode(val=1, next=None)
node2 = ListNode(val=2, next=None)
node3 = ListNode(val=3, next=None)
node4 = ListNode(val=4, next=None)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2
# Since in the print __str__ of the ListNode it goes forever it prints infinately
print("1st test case", sol.getLoopHead(node1).val)
# Test case 2
# print("2nd test case", sol.func())
# Test case 3
# print("3rd test case", sol.func())
