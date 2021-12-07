class Stack:
  def __init__(self):
    self.list = []

  def push(self, value):
    self.list.append(value)
    return value
  
  def pop(self):
    ele = self.list[-1]
    self.list.pop()
    return ele
  
  def peek(self):
    print(self.list[-1])
  

obj1 =  Stack()
obj1.push(10)
obj1.push(20)
obj1.push(30)
obj1.push(40)
obj1.push(50)

print(obj1.list)

obj1.peek()
obj1.pop()
print(obj1.list)
obj1.pop()
print(obj1.list)
obj1.pop()
print(obj1.list)
obj1.pop()
print(obj1.list)
obj1.pop()
print(obj1.list)



