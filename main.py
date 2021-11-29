class Node:
  def __init__(self, value):
    self.value = value
    self.next = None
    self.prev = None
  

obj1 = Node(10)
obj2 = Node(11)
# obj3 = Node(12)


obj2.prev = obj1
obj1.next = obj2

print(obj1.value)
print(obj1.next)
print(obj1.prev)

print(obj1.next.value)
print(obj1.next.next)
print(obj1.next.prev)


print(obj1.next.prev.value)
print(obj1.next.prev.next)
print(obj1.next.prev.prev)

    

