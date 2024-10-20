# Problem:
# Animal Shelter: An animal shelter, which holds only dogs and cats,
# operates on a strictly "first in, first out" basis. People must 
# adopt either the "oldest" (based on arrival time) of all animals
# at the shelter, or they can select whether they would prefer a dog 
# or a cat (and will receive the oldest animal of that type). They 
# cannot select which specific animal they would like. Create the 
# data structures to maintain this system and implement operations 
# such as enqueue, dequeueAny, dequeueDog, and dequeueCat. You may 
# use the built-in Linkedlist data structure.s

# Brainstorming:
#

class Node:
  def __init__(self, data, next=None):
    self.data = data
    self.next = next

  def __str__(self):
    return str(self.data)
  
class LinkedList:
  def __init__(self, head=None):
    self.head = head

  def insert(self, node):
    if self.head is None:
      self.head = node
      return
    current_node = self.head
    while current_node.next != None:
      current_node = current_node.next
    current_node.next = node

  def peek(self):
    return self.head

  def pop(self):
    if self.head:
      node = self.head
      self.head  = self.head.next
      return node
    return None
  
  def size(self):
    current_node = self.head
    size = 0
    while current_node != None:
      size += 1
      current_node = current_node.next
    return size

  def __str__(self):
    current_node = self.head
    s = ""
    while current_node != None:
      s += str(current_node) + " "
      current_node = current_node.next
    return s

class Animal:
  def __init__(self, order, name):
    self.order = order
    self.name = name

  def isOlder(self, animal):
    return self.order < animal.order
  
  def __str__(self):
    return "(" + str(self.name) + " " + str(self.order) + ")"

class Dog(Animal):
  pass

class Cat(Animal):
  pass


class AnimalQueue:
  def __init__(self):
    self.dogs = LinkedList()
    self.cats = LinkedList()
    self.order = 0

  def enqueue(self, animal: Animal):
    animal.order = self.order
    self.order += 1

    if isinstance(animal, Dog): self.dogs.insert(Node(animal))
    elif isinstance(animal, Cat): self.cats.insert(Node(animal))

  def dequeueAny(self):
    if self.dogs.size() == 0:
      return self.dequeuCat()
    elif self.cats.size() == 0:
      return self.dequeueDog()
    
    dog = self.dogs.peek()
    cat = self.cats.peek()
    if dog.data.isOlder(cat.data):
      return self.dequeueDog()
    else:
      return self.dequeuCat()

  def dequeueDog(self):
    return self.dogs.pop()

  def dequeuCat(self):
    return self.cats.pop()
  
  def __str__(self):
    return str(self.dogs) + str(self.cats)

class Solution:
  def test(self):
    dog = Dog(-1, "dog")
    cat = Cat(-1, "cat")
    q = AnimalQueue()
    # q.enqueue(cat)
    # q.enqueue(dog)
    # print(q)
    # print("Dequeu cat " + str(q.dequeuCat()))
    # print("Dequeu cat " + str(q.dequeuCat()))
    # print("Dequeu dog " + str(q.dequeueDog()))
    # print("Dequeu dog " + str(q.dequeueDog()))

    q.enqueue(cat)
    q.enqueue(dog)
    q.enqueue(Dog(-1, "dog1"))
    q.enqueue(Dog(-1, "dog2"))
    q.enqueue(Cat(-1, "cat1"))
    q.enqueue(Dog(-1, "cat2"))
    print(q)
    print(q.dequeueAny())
    

# Test
sol = Solution()
# Test case 1
print("1st test case", sol.test())
