# Problem:
# Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high,
# it might topple. Therefore, in real life, we would likely start a new stack when 
# the previous stack exceeds some threshold. Implement a data structure SetOfStacks 
# that mimics this. SetOfStacks should be composed of several stacks and should 
# create a new stack once the previous one exceeds capacity. 
# SetOfStacks.push() and SetOfStacks.pop() should behave identically to a single
# stack (that is, pop () should return the same values as it would if there were 
# just a single stack).
# FOLLOW UP:
# Implement a function popAt(int index) which performs a pop operation on a specific 
# substack.

# Brainstorming:
# keep in mind that when last stack is empty after pop, it should be deleted from the 
# set. When pushing check the length of the last stack in the set.
# Split the code into functions: getLastStack(), isFull() and etc.

class Node:
    def __init__(self, value):
        self.value = value
        self.above = None
        self.below = None

class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.top = None
        self.bottom = None

    def is_full(self):
        return self.size == self.capacity

    def is_empty(self):
        return self.size == 0

    def join(self, above, below):
        if below:
            below.above = above
        if above:
            above.below = below

    def push(self, v):
        if self.size >= self.capacity:
            return False
        self.size += 1
        n = Node(v)
        if self.size == 1:
            self.bottom = n
        self.join(n, self.top)
        self.top = n
        return True

    def pop(self):
        if not self.top:
            return None
        t = self.top
        self.top = self.top.below
        self.size -= 1
        return t.value

    def remove_bottom(self):
        b = self.bottom
        self.bottom = self.bottom.above
        if self.bottom:
            self.bottom.below = None
        self.size -= 1
        return b.value

class SetOfStacks:
  def __init__(self, capacity):
    self.capacity = capacity
    self.stacks = []

  def get_last_stack(self):
    if not self.stacks:
      return None
    return self.stacks[-1]

  def is_empty(self):
    last = self.get_last_stack()
    return not last or last.is_empty()

  def push(self, v):
    last = self.get_last_stack()
    if last and not last.is_full():
      last.push(v)
    else:
      stack = Stack(self.capacity)
      stack.push(v)
      self.stacks.append(stack)

  def pop(self):
    last = self.get_last_stack()
    if not last:
      return None
    v = last.pop()
    if last.size == 0:
      del self.stacks[-1]
    return v

  def pop_at(self, index):
    return self.left_shift(index, True)

  def left_shift(self, index, remove_top):
    stack = self.stacks[index]
    removed_item = stack.pop() if remove_top else stack.remove_bottom()
    if stack.is_empty():
      del self.stacks[index]
    elif len(self.stacks) > index + 1:
      v = self.left_shift(index + 1, False)
      stack.push(v)
    return removed_item

  
class Solution:
  def test(self):
    stacks = SetOfStacks(2)
    stacks.push(1)
    stacks.push(2)
    stacks.push(3)
    stacks.push(4)
    stacks.push(5)
    print(stacks)
    stacks.pop()
    print(stacks)
    stacks.pop()
    stacks.pop()
    print(stacks)
    stacks.push(5)
    print(stacks)
    
# Test
sol = Solution()
sol.test()