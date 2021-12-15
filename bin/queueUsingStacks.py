"""
  queue using stacks

stack - Last in first out
	s1 = [ 1 2 3 4 5 ]
push - insert in the last
	push(6)

	s1 = [ 1 2 3 4 5 6 ]
pop() - delete at the lsat
	s1 = [ 1 2 3 4 5 ]

queue -- first in first out

s1 = [ 1 2 3 4 5 ] 

enqueue(6) insert in the last
s1 = [ 1 2 3 4 5 6 ]

dequeue()
s2 = [ 2 3 4 5 6 ]


common part - push and insert will be happening at last
dequeue is varying:


s1 = 1 2 3 4 5 6
s2 = 6 5 4 3 2 1 

pop()

s2 = 6 5 4 3 2

s1 =  2 3 4 5 6


"""

class Queue:
  def __init__(self):
    self.stack1 = []
    self.stack2 = []
  
  def push(self, value):
    self.value = value
    self.stack1.append(self.value)
    return self.value
  
  def pop(self):
    self.stack1.pop()
  
  def print(self):
    print(self.stack1)

  def enqueue(self, value):
    self.valueQ = value
    self.push(self.valueQ)
    return self.valueQ
  
  def reverseList(self, inputXs, outputXs):
    while inputXs:
      item = inputXs[-1]
      outputXs.append(item)
      inputXs.pop()
    return outputXs

  
  def deQueue(self):
    self.reverseList(self.stack1, self.stack2)
    self.stack2.pop()
    self.reverseList(self.stack2, self.stack1)
    return self.stack1


obj1 = Queue()
obj1.enqueue(10)
obj1.enqueue(20)
obj1.enqueue(30)
obj1.print()
obj1.deQueue()
obj1.print()
obj1.deQueue()    
obj1.print()




  
  

