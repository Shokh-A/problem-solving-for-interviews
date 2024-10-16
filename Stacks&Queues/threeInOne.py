

# Problem:
# Three in One: Describe how you could use a single array to implement three stacks.

# Brainstorming:
# The implementation depends on several factors:
# Do stacks take up certain given space?
# Should all stacks have equal space allocated in the array
# Can one stack have more space allocated to it?
# Raise errors where necessary.
# Keep code clean and readable
# Separate functionalities

class FixedMultiStack:
  def __init__(self, stackSize: int):
    self.number_of_stacks = 3
    self.stackCapacity = stackSize
    self.values = [0] * stackSize * self.number_of_stacks
    self.sizes = [0] * self.number_of_stacks

  def push(self, stackNum: int, value: int) -> None:
    if self.__isFull(stackNum):
      raise FullStackException()

    self.sizes[stackNum] += 1
    self.values[self.__indexOfTop(stackNum)] = value

  def pop(self, stackNum: int) -> int:
    if self.isEmpty(stackNum):
      raise EmptyStackException()
    
    topIndex = self.__indexOfTop(stackNum)
    value = self.values[topIndex]
    self.values[topIndex] = 0
    self.sizes[stackNum] -= 1
    return value
  
  def peek(self, stackNum: int):
    if self.isEmpty(stackNum):
      raise EmptyStackException()
    return self.values[self.__indexOfTop(stackNum)]
    
  def isEmpty(self, stackNum: int):
    return self.sizes[stackNum] == 0
    
  def __isFull(self, stackNum: int):
    return self.sizes[stackNum] == self.stackCapacity
  
  def __indexOfTop(self, stackNum: int):
    offset = stackNum * self.stackCapacity
    size = self.sizes[stackNum]
    return offset + size - 1

  
class MultiStackError(Exception):
  """MultiStack operation error"""

class FullStackException(MultiStackError):
  """FullStackException error"""

class EmptyStackException(MultiStackError):
  """EmptyStackException error"""

class Solution:

  def func(self):
    stacks = FixedMultiStack(5)

    try:
      stacks.pop(0)
    except EmptyStackException:
      print("Stack is empty!")

    try:
      stacks.peek(0)
    except EmptyStackException:
      print("Stack is empty!")

    stacks.push(0, 1)
    stacks.push(1, 1)
    stacks.push(2, 1)
    print(stacks.values)

    stacks.push(0, 2)
    stacks.push(1, 2)
    stacks.push(2, 2)

    print(stacks.values)
    print(stacks.peek(0))

    print(stacks.pop(2))
    print(stacks.values)

    stacks.push(0, 3)
    stacks.push(0, 4)
    stacks.push(0, 5)
    print(stacks.values)
    
    try:
      stacks.push(0, 6)
    except FullStackException:
      print("Stack is full!")


# Test
sol = Solution()
# Test case 1
print("1st test case", sol.func())
# Test case 2
# print("2nd test case", sol.func())
# Test case 3
# print("3rd test case", sol.func())
