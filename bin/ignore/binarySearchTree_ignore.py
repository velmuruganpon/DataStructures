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
    self.counter = 1
  
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
    currentNode = self.root    
    while True:
      currentValue = currentNode.value
      if value < currentValue:
        if not currentNode.left:
          print("No node with value {0}".format(value))
          return
        currentNode = currentNode.left
      elif value > currentValue:
        if not currentNode.right:
          print("No node with value {0}".format(value))
          return
        currentNode = currentNode.right
      else:
        print("Match Found {0}".format(value))
        return currentNode

  def minLeft(self, node):
    parentLeftNode = None
    temp = node.left
    leftNode = None
    while True:
      if not temp:
        return leftNode, parentLeftNode
      else:
        parentLeftNode = leftNode
      leftNode = temp
      temp = temp.left

  def remove(self, value):
    currentNode = self.root
    parentNode = None  
    while currentNode!= None and currentNode.value != value:
      parentNode = currentNode
      if value < currentNode.value:
        currentNode = currentNode.left
      else:
        currentNode = currentNode.right
    if not currentNode:
      print("No key")
      return self.root
    leftNode = currentNode.left 
    rightNode = currentNode.right

    if not leftNode or not rightNode:  
      if not leftNode and not rightNode:
        nodeToBe = None
      elif not rightNode:
        nodeToBe  = currentNode.left
      elif not leftNode:
        nodeToBe = currentNode.right
      
      if parentNode.left == currentNode:
        parentNode.left = nodeToBe
      elif parentNode.right ==  currentNode:
        parentNode.right = nodeToBe
      else:
        print("No node with given key...")  
    else:
      if rightNode.left:
        leftMostNode, parentLeftMostNode = self.minLeft(rightNode)
        parentLeftMostNode = parentLeftMostNode if parentLeftMostNode else rightNode
        if leftMostNode.right:
          parentLeftMostNode.left = leftMostNode.right
        else:
          parentLeftMostNode.left = None
        currentNode.value = leftMostNode.value        
      else:
        currentNode.value = rightNode.value
    return self.root


  def printHTree(self, node, space):

    if node == None:
      return
    
    leftNode = node.left 
    rightNode = node.right

    height = math.ceil(self.length/2)
    
    space = height + space
    self.printHTree(rightNode, space)

    print()
    for i in range(0, space):
      print(end=' ')

    print(node.value)

    self.printHTree(leftNode, space)
     

obj1 = BST(100)
obj1.insert(25)
obj1.insert(150)
obj1.insert(12)
obj1.insert(35)

obj1.insert(6)
obj1.insert(18)

obj1.insert(30)
obj1.insert(70)

obj1.insert(130)
obj1.insert(180)

obj1.insert(115)
obj1.insert(135)



obj1.insert(155)
obj1.insert(205)

obj1.insert(168)

obj1.insert(167)
obj1.insert(170)



obj1.printHTree(obj1.root, 0)
# delete 150 
# right child(180) to 150 contains right(205)
# right child(180) to 150 contains left(155)
# 155 didnt contain left but it has right(168) 
# after delete
# 155 came to 150th position and 168 came to 155th position

print ( "+++++++++++++++++++++++++++++++++++++++++++")
obj1.remove(150)
obj1.printHTree(obj1.root, 0)

print ( "+++++++++++++++++++++++++++++++++++++++++++")
obj1.remove(6)
obj1.printHTree(obj1.root, 0)


print ( "+++++++++++++++++++++++++++++++++++++++++++")
obj1.remove(100)
obj1.printHTree(obj1.root, 0)


print ( "+++++++++++++++++++++++++++++++++++++++++++")
obj1.remove(180)
obj1.printHTree(obj1.root, 0)

print ( "+++++++++++++++++++++++++++++++++++++++++++")
obj1.remove(130)
obj1.printHTree(obj1.root, 0)

print ( "+++++++++++++++++++++++++++++++++++++++++++")
obj1.remove(205)
obj1.printHTree(obj1.root, 0)

print ( "+++++++++++++++++++++++++++++++++++++++++++")
obj1.remove(25)
obj1.printHTree(obj1.root, 0)

print ( "+++++++++++++++++++++++++++++++++++++++++++")
obj1.remove(12)
obj1.printHTree(obj1.root, 0)


print ( "+++++++++++++++++++++++++++++++++++++++++++")
obj1.remove(30)
obj1.printHTree(obj1.root, 0)






    


