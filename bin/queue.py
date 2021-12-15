class Node:
  def __init__(self,value):
    self.value =  value
    self.next = None

class Queue:
  def __init__(self,value):
    self.value = value
    self.front = Node(self.value)
    self.back = self.front
    self.length = 1
  
  def push(self, value):
    self.value = value
    self.newNode = Node(self.value)
    self.newNode.next = self.front
    self.front = self.newNode
    self.length = self.length + 1
    return self.front
  
  def pop(self):
    if self.length > 0: 
      self.currentNode = self.front
      self.nextNode = self.currentNode.next
      self.front = self.nextNode
      self.length = self.length - 1
    else:
      print("No item in the list. length is less than 1")
    return self.front
  
  def hasNext(self, node):
    self.node = node
    return True if self.node.next else False

  def print(self):
    self.xs = []
    currentNode = self.front
    
    while self.hasNext(currentNode):
      self.xs.append(currentNode.value)
      currentNode = currentNode.next
    self.xs.append(currentNode.value)
    print(self.xs)
    return self.xs


obj1 =  Queue(10)
obj1.print()
obj1.push(20)
obj1.push(30)
obj1.push(40)
obj1.print()
obj1.pop()
obj1.pop() 
obj1.print()   

