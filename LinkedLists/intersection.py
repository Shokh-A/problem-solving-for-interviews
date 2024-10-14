

# Problem:
# Intersection: Given two (singly) linked lists, determine if the two lists intersect. Return the
# intersecting node. Note that the intersection is defined based on reference, not value. That is,
# if the kth node of the first linked list is the exact same node (by reference) as the jth node 
# of the second linked list, then they are intersecting.

# Brainstorming:
# Brute force solution would be to check for every element in the first list, if it exists in the
# second list.
# If two linked lists intersect they are supposed to have the same tail.

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

  # Brute force
  # Time - O(n^2)
  def intersect(self, l1: ListNode, l2: ListNode) -> ListNode:
    head = l2
    while l1 != None:
      while l2 != None:
        if l1 == l2:
          return l1
        l2 = l2.next
      l1 = l1.next
      l2 = head
    return None
  
  # Optimal
  # Time - O(A + B), where A and B are the lenghts of the linked lists.
  # Space - O(1)
  def intersection(self, l1: ListNode, l2: ListNode) -> ListNode:
    if l1 == None or l2 == None:
      return None
    
    tail1, size1 = self.getTailAndSize(l1)
    tail2, size2 = self.getTailAndSize(l2)

    if tail1 != tail2:
      return None
    
    shorter = l1 if size1 < size2 else l2
    longer = l2 if size1 < size2 else l1

    longer = self.getKthNode(longer, abs(size1 - size2))

    while shorter != longer:
      shorter = shorter.next
      longer = longer.next

    return longer

  
  def getTailAndSize(self, node: ListNode):
    if node == None:
      return None
    
    size = 1
    current = node
    while current.next != None:
      size += 1
      current = current.next
    
    return current, size
    
  def getKthNode(self, node: ListNode, k: int) -> ListNode:
    current = node
    while k > 0 and current != None:
      current = current.next
      k -= 1
    return current

# Test
sol = Solution()
# Test case 1
intersection = ListNode(val=50, next=
               ListNode(val=3, next=
               ListNode(val=4, next=None)))
l1 = ListNode(val=1, next=
     ListNode(val=2, next=intersection))
l2 = ListNode(val=1, next=
     ListNode(val=2, next=intersection))
print("1st test case", sol.intersection(l1, l2))
# Test case 2
# print("2nd test case", sol.func())
# Test case 3
# print("3rd test case", sol.func())
