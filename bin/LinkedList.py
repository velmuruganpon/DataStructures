import sys

class Node:
  def __init__(self,value):
    self.value = value
    self.next = None

class LinkedList:
  def __init__(self,value):
    self.value = value
    self.node = Node(self.value)
    self.head = self.node
    self.tail = self.node
    self.length = 1
  
  def print(self):
    xs = []
    currentNode = self.head
    xs.append(currentNode.value)
    while currentNode.next != None:
      currentNode = currentNode.next
      xs.append(currentNode.value)
    print(xs)
    return None
  
  def traverseToNode(self,pos):
    counter = 1
    currentNode = self.head
    while counter != pos:
      currentNode = currentNode.next
      counter = counter + 1
    return currentNode

  
  def insert(self, pos,  value):
    newNode = Node(value)
    if pos < 1:
      print("position should start from 1")
      sys.exit(-1)

    if pos == 1:
      currentNode = self.head
      newNode.next = currentNode
      self.head = newNode
    elif pos > 1 and pos <= self.length:
      currentNode = self.traverseToNode(pos - 1) 
      newNode.next = currentNode.next
      currentNode.next = newNode
    else:
      self.tail.next = newNode
      self.tail = newNode
    self.length = self.length + 1
    return None


  def delete(self,pos):
    if pos < 1:
      print("position should start from 1")
      sys.exit(-1)

    if pos == 1:
      currentNode = self.head
      self.head = currentNode.next
    elif pos > 1 and pos <= self.length:
      currentNode = self.traverseToNode(pos - 1) 
      nodeTobeDeleted = currentNode.next
      currentNode.next = nodeTobeDeleted.next
    else:
      print("position should be <= {0}".format(self.length))
      sys.exit(-1)
    self.length = self.length - 1
    return None






lxs = LinkedList(10)
lxs.insert(1,5)
lxs.print()
lxs.insert(1,3)
lxs.print()
lxs.insert(2,3)
lxs.print()
lxs.insert(4,55)
lxs.print()
lxs.insert(4,54)
lxs.print()
lxs.insert(10,54)
lxs.insert(1,11)
lxs.print()
print(lxs.__dict__)
lxs.delete(1)
lxs.print()
lxs.delete(1)
lxs.print()
lxs.delete(5)
lxs.print()
lxs.delete(5)
lxs.print()
lxs.delete(99)
lxs.print()
