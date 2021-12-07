class Node:
  def __init__(self,value):
    self.value = value
    self.next = None

class Stack:
  def __init__(self,value):
    self.value = value
    self.top = Node(self.value)
    self.bottom = self.top
    self.length = 1

  def push(self, value):
    """
    Last In First Out
    """
    self.value = value
    # Last In 
    self.currentNode = Node(self.value)
    topNode =  self.top
    self.top = self.currentNode
    self.top.next = topNode
    self.length = self.length + 1
    return self.top.value
    
  def pop(self):
    # First out
    topValue = self.top.next
    self.top = topValue
    return self.top.value
  
  def peek(self):
    # print the top Value 
    return self.top.value

  def hasNext(self, node):
    self.node = node
    return True if self.node.next else False
  
  def print(self):
    xs = []
    self.currentNode = self.top
    while self.hasNext(self.currentNode):
      xs.append(self.currentNode.value)
      self.currentNode = self.currentNode.next
    xs.append(self.currentNode.value)
    print(xs)
    return None


obj1 = Stack(10)
obj1.print()
obj1.push(11)
obj1.push(21)
obj1.push(31)
obj1.push(41)
obj1.print()
print(obj1.peek())
obj1.pop()
obj1.print()
obj1.pop()
obj1.print()
obj1.pop()
obj1.print()
obj1.pop()
obj1.print()


      
