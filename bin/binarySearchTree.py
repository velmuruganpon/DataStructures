import math

class Node:
  def __init__(self,value):
    self.value = value
    self.left = None
    self.right = None

class BST:
  def __init__(self, value):
    self.value = value
    self.node = Node(self.value)
    self.root = self.node
    self.length = 1
  
  def insert(self, value):
    self.value = value
    newNode = Node(self.value)
    currentNode = self.root
    
    while True:
      currentValue = currentNode.value
      if value < currentValue:
        #left 
        if not currentNode.left:
          currentNode.left = newNode
          self.length = self.length + 1
          return 
        currentNode = currentNode.left
      else:
        # right
        if not currentNode.right:
          currentNode.right = newNode
          self.length = self.length + 1
          return
        currentNode = currentNode.right

  def lookup(self,value):
    self.value = value
    self.currentNode = self.root
    
    while True:
      currentValue = self.currentNode.value
      if value < currentValue:
        if not self.currentNode.left:
          print("No node with value {0}".format(value))
          return
        self.currentNode = self.currentNode.left
      elif value > currentValue:
        if not self.currentNode.right:
          print("No node with value {0}".format(value))
          return
        self.currentNode = self.currentNode.right
      else:
        print("Match Found {0}".format(value))
        return self.currentNode

  def print(self):
    self.currentNode = self.root
    self.leftNode = self.currentNode.left if self.currentNode.left else None
    self.rightNode = self.currentNode.right if self.currentNode.right else None
    self.height = math.ceil(self.length/2)
    self.count = 1
    print(self.root.value)

    while True:
      if self.leftNode:
        print(self.leftNode.value)
        self.leftNode = self.leftNode.left
      

      




    



obj1 = BST(10)
obj1.insert(25)
obj1.insert(22)

obj1.print(obj1.root)



    


