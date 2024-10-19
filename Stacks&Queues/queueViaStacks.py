# Problem:
# Queue via Stacks: Implement a MyQueue class which implements a queue using two stacks.

# Brainstorming:
#

from stack import Stack

class MyQueue:
  def __init__(self):
    self.stackNewest = Stack()
    self.stackOldest = Stack()

  def add(self, value):
    self.stackNewest.push(value)

  def shiftStacks(self):
    if self.stackOldest.is_empty():
      while not self.stackNewest.is_empty():
        self.stackOldest.push(self.stackNewest.pop())

  def peek(self):
    self.shiftStacks()
    return self.stackOldest.peek()
  
  def remove(self):
    self.shiftStacks()
    return self.stackOldest.pop()
  
  def is_empty(self):
    return len(self) == 0
  
  def __len__(self):
    return len(self.stackOldest) + len(self.stackNewest)


class Solution:
  def test(self):
    q = MyQueue()
    q.add(5)
    q.add(2)
    q.add(3)
    print(q.peek())
    print(q.remove())
    print(q.peek())

# Test
sol = Solution()
# Test case 1
print("1st test case", sol.test())
