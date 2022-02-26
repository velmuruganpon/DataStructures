import json


def printObj(A):
  json_data = json.dumps(A,default=lambda o: o.__dict__, indent =  4)
  bstJson = json.loads(json_data)
  print(bstJson)
  

class Node:
  def __init__(self,value):
    self.value =  value
    self.left = None
    self.right = None


class BST:
  def __init__(self):
    self.root = None

  def insert(self,value):
    node = Node(value)
    if not self.root:
      self.root = node
    else:
      currentNode = self.root
      while(True):
        if value < currentNode.value:
          if not currentNode.left:
            currentNode.left = node
            return
          currentNode = currentNode.left 
        else:        
          if not currentNode.right:
            currentNode.right = node
            return
          currentNode =  currentNode.right

  def lookup(self, value):
    # getting currentNode and ParentNode
    parentNode = None
    node = self.root    
    while(True):
      # print(node.value)
      if not self.root:
        return         

      if value < node.value:
        if not node.left:
          print("match not found")
          return
        parentNode = node
        node = node.left
      elif value > node.value:
        if not node.right:
          print("match not found")
          return
        parentNode = node
        node = node.right
      elif value == node.value:
        print("match found")
        return [ node, parentNode ]

  def minNode(self,node):
    currentNode = node
    parentNode = None
    while(True):
      if not(currentNode.left and currentNode.right):
        return [ currentNode, parentNode ]
      elif currentNode.left:
        parentNode = currentNode
        currentNode = currentNode.left
        return [ currentNode, parentNode ]
      elif currentNode.right:
        parentNode = currentNode
        currentNode =  currentNode.right

  
  def remove(self, value):
    # node to be deleted has no children
    # remove that node 

    nodes = self.lookup(value)

    if nodes:
      node = nodes[0]
      # print("node to be deleted")
      # printObj(node)
      # print("parent node for node to be deleted")
      parentNode = nodes[1]
      # printObj(parentNode)

      if not (node.left and node.right):
        print("scenario 1 : no children")
        if not parentNode:
          # we have only root node without childrens
          self.root = None
        elif parentNode.left == node:
          parentNode.left = None
        elif parentNode.right == node:
          parentNode.right = None
    # if node to be deleted has one child only
      elif ( node.left and not node.right ) or ( node.right and not node.left):
        print("scenario 2 : any one child")
        childNode =  node.left if node.left else node.right
        if not parentNode:
          # node to be deleted is root
          self.root = childNode
        elif parentNode.left == node:
          # 10 --> 6 -->  4 --> 7
          # remove(6) 
          # 10 --> 4 --> 7
          parentNode.left = childNode
        elif parentNode.right == node:
          # 10  --> 15 --> 13 -->14
          # remove(15)
          # 10 --> 13 -->14
          parentNode.right = childNode

    # if node to be deleted has two children
    # find out the minimum node in the right sub tree of "nodes to be deleted"
    # copy value content from the minimum node and replace with the "node to be deleted"
    # remove the minimum node 
      elif node.left and node.right :
      # go to right Node
        print("scenario 3: two children")
        nodeDotRightTree = node.right
        minimumNodeOfRightTree = self.minNode(nodeDotRightTree)
        minimumNodeOfRightTreeLeaf = minimumNodeOfRightTree[0]
        minimumNodeOfRightTreeParent = minimumNodeOfRightTree[1] if minimumNodeOfRightTree[1] else node
        node.value = minimumNodeOfRightTreeLeaf.value
        if minimumNodeOfRightTreeParent.left == minimumNodeOfRightTreeLeaf:
          minimumNodeOfRightTreeParent.left = None
        elif minimumNodeOfRightTreeParent.right == minimumNodeOfRightTreeLeaf:
          minimumNodeOfRightTreeParent.right = None
    return self.root


# scenario 1
obj1 = BST()
obj1.insert(40)

print ("before remove 40")
printObj(obj1)
obj1.remove(40)
print ("after remove")
printObj(obj1)
print("================================")
print("================================")

obj1 = BST()
obj1.insert(40)
obj1.insert(20)
obj1.insert(80)
obj1.insert(60)
obj1.insert(100)


print ("before remove 60")
printObj(obj1)
obj1.remove(60)
print ("after remove")
printObj(obj1)
print("================================")
print("================================")

      
obj1 = BST()
obj1.insert(40)
obj1.insert(20)
obj1.insert(80)
obj1.insert(60)
obj1.insert(100)

print ("before remove 40")
printObj(obj1)
obj1.remove(40)
print ("after remove")
printObj(obj1)
print("================================")
print("================================")


obj1 = BST()
obj1.insert(40)

print ("before remove 500")
printObj(obj1)
obj1.remove(500)
print ("after remove")
printObj(obj1)
print("================================")
print("================================")

      


  
    