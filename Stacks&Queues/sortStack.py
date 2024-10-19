# Problem:
# Sort Stack: Write a program to sort a stack such that the smallest items are
# on the top. You can use an additional temporary stack, but you may not copy 
# the elements into any other data structure (such as an array). The stack 
# supports the following operations: push, pop, peek, and isEmpty.

# Brainstorming:
# Stacks are like annoying game advertisement with pourting different color of
# luqiud from one bottle to another until all colors match in bottle.

from stack import Stack

class Solution:
  def sortStack(self, stack: Stack):
    sortedStack = Stack()
    while not stack.is_empty():
      pop = stack.pop()
      while not sortedStack.is_empty() and pop > sortedStack.peek():
        stack.push(sortedStack.pop())
      sortedStack.push(pop)

    return sortedStack
      
    


# Test
sol = Solution()
# Test case 1
stack = Stack()
stack.push(4)
stack.push(1)
stack.push(3)
stack.push(5)
stack.push(2)
print("1st test case", sol.sortStack(stack))