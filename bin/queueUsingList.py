class Queue:
  def __init__(self):
    self.xs =[]
  
  def push(self, value):
    return self.xs.insert(0,value)
  
  def pop(self):
    return self.xs.pop(0)
  
  def print(self):
    print(self.xs)
  

obj1 = Queue()
obj1.push(10)
obj1.push(20)
obj1.push(30)
obj1.print()
obj1.pop()
obj1.pop()
obj1.print()



  
  
