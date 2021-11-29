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
  
  def reverse(self):
    if self.length > 1:
      first = self.head
      second = first.next
      while second:
        temp = second.next
        second.next = first
        first = second
        second = temp
      self.head.next = None
      self.head = first
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
lxs.reverse()
lxs.print()

"""
{ 
value : 1
next : {
				value : 2
				next  : {
							value : 3 
							next : {
										value : 4
										next : {
													value : 5
													next : None
												}
									}
					}
		}
}


second.next = first


value : 2
next  : { 
		value : 1
		next : {
						value : 2
						next  : {
									value : 3 
									next : {
												value : 4
												next : {
															value : 5
															next : None
														}
											}
							}
				}
		}

		
			
				
first = second
value : 2
next  : { 
		value : 1
		next : {
						value : 2
						next  : {
									value : 3 
									next : {
												value : 4
												next : {
															value : 5
															next : None
														}
											}
							}
				}
		}

second:
{
value : 3 
next : {
			value : 4
			next : {
						value : 5
						next : None
					}
		}


}
							

first = head  # 1 2 3 4 5
second = first.next # 2 3 4 5

while second

iteration 1:

	temp = second.next # 3 4 5
	second.next = first  # value = 2 , next = { value = 1 , next = 1 , 2, 3, 4, 5 }
	first = second #  # value = 2 , next = { value = 1 , next = 1 , 2, 3, 4, 5 }
	second = temp # value 3 4 5
	
first = second #  # value = 2 , next = { value = 1 , next = 1 , 2, 3, 4, 5 }
second = # 3 4 5
iteration 2:
	temp = second.next # 4 5
	second.next = first  # value = 3 , next = { value = 2 , next = 1 , 2, 3, 4, 5 }
	first = second #  # value = 3 , next = { value = 2 , next = { value = 1 , next = 1 , 2, 3, 4, 5 } }
	second = temp # value 4 5

first = second #  # value = 3 , next = { value = 2 , next = { value = 1 , next = 1 , 2, 3, 4, 5 } }
second = # 4 5
iteraion 3:
	temp = second.next #5 next null
	second.next = first # value = 3 , next = { value = 2 , next = { value = 1 , next = 1 , 2, 3, 4, 5 } }
	first = second # value = 4, next =  { value = 3 , next = { value = 2 , next = { value = 1 , next = 1 , 2, 3, 4, 5 } } }
	second = temp

first = second # value = 4, next =  { value = 3 , next = { value = 2 , next = { value = 1 , next = 1 , 2, 3, 4, 5 } } }
second = # 5 null

iteration 4:
	temp = second.next #null
	second.next = first # value = 4, next =  { value = 3 , next = { value = 2 , next = { value = 1 , next = 1 , 2, 3, 4, 5 } } }
	first = second  value = 5 , next = { value = 4, next =  { value = 3 , next = { value = 2 , next = { value = 1 , next = 1 , 2, 3, 4, 5 } } } }
	second = temp


self.head.next = null
self.head = first
"""