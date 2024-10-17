

# Problem:
# Stack Min: How would you design a stack which, in addition to push and pop, has a function min
# which returns the minimum element? Push, pop and min should all operate in 0(1) time.

# Brainstorming:
# 

from stack import Stack

class MinStack(Stack):
  def __init__(self):
    super().__init__()
    self.minvals = Stack()

  def push(self, value):
    super().push(value)
    if not self.minvals or value <= self.minimum():
      self.minvals.push(value)

  def pop(self):
    value = super().pop()
    if value == self.minimum():
      self.minvals.pop()
    return value
  
  def minimum(self):
    return self.minvals.peek()


class Solution:
  def test(self):
    stack = MinStack()
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(1)
    return stack.minimum()
    # stack.pop()
    # return stack.minimum()

# Test
sol = Solution()
# Test case 1
print("1st test case", sol.test())
