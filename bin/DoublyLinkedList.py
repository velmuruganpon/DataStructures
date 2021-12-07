import sys

class Node:
  def __init__(self,value):
    self.value = value
    self.next = None
    self.prev = None


class DoublyLinkedList:
  def __init__(self,value):
    self.value = value
    self.head = Node(self.value)
    self.tail = self.head
    self.length = 1

  def traverseToNode(self, pos):
    counter = 1
    currentNode = self.head
    while counter != pos:
      currentNode = currentNode.next
      counter = counter + 1
    return currentNode

  def insert(self, pos, value):
    self.value = value
    self.newNode = Node(self.value)
    if pos <= 0:
      print("Position should start from 1")
      sys.exit(-1)
    elif pos == 1:
      currentNode = self.head
      self.newNode.next = currentNode
      currentNode.prev = self.newNode
      self.head = self.newNode
    elif pos > 1 and pos <= self.length:
      currentNode = self.traverseToNode(pos - 1)
      self.newNode.next = currentNode.next
      self.newNode.prev = currentNode
      currentNode.next = self.newNode
    else:
      currentNode = self.newNode
      print("NewNode value {0}".format(currentNode.value))
      prevNode = self.tail
      print("PrevNode value {0}".format(prevNode.value))
      currentNode.prev = prevNode
      prevNode.next = currentNode
      self.tail = currentNode
    self.length = self.length + 1
    return self.value
    
  def printList(self):
    xs = []
    xs1 = []
    currentNode = self.head
    counter = 1
    while counter <= self.length:
      subXs = []
      prevNode = currentNode.prev
      currentValue = currentNode.value if currentNode else None
      prevValue = prevNode.value if prevNode else None
      subXs.append(prevValue)
      subXs.append(currentValue)
      xs.append(subXs)
      xs1.append(currentValue)
      currentNode = currentNode.next
      counter = counter + 1
    print(xs)
    print(xs1)
    return xs1
  
  def print(self):
    xs = []
    currentNode = self.head
    xs.append(currentNode.value)
    while currentNode.next != None:
      currentNode = currentNode.next
      xs.append(currentNode.value)
    print(xs)
    return None
  
  def delete(self, pos):
    if pos == 0:
      print("Position should be greater than 0")
      sys.exit(-1)
    elif pos > self.length:
      print("Length of the linked list is {0}".format(self.length))
      sys.exit(-1)
    
    currentNode = self.traverseToNode(pos)
    prevNode = currentNode.prev
    nextNode = currentNode.next

    if pos == 1:
      nextNode.prev = None
      self.head = nextNode
    elif pos > 1 and pos < self.length:
      prevNode.next = nextNode
      nextNode.prev = prevNode
    elif pos == self.length:
      prevNode.next = None
      self.tail = prevNode
    self.length = self.length -1 
    return pos

  def reverse(self):
    xs = []
    currentNode = self.tail
    counter = self.length
    while counter >= 1:
      value = currentNode.value
      xs.append(value)
      currentNode = currentNode.prev
      counter = counter - 1
    print(xs)
    
    return xs


    

  
obj1 = DoublyLinkedList(10)
print("inserting 12 at position 3...")
obj1.insert(3,12)
obj1.printList()
print("inserting 12 at position 4...")
obj1.insert(4,12)
obj1.printList()
print("inserting 15 at position 4...")
obj1.insert(4,16)
obj1.printList()
obj1.insert(5,17)
obj1.printList()
obj1.print()
print("inserting 9 at position 1...")
obj1.insert(1,9)
obj1.printList()
obj1.print()
print("Deleting the 4th element...")
obj1.delete(4)
obj1.printList()
obj1.print()
obj1.reverse()




     
      
      

