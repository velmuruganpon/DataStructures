class MyList:
  def __init__(self):
    self.length = 0
    self.data = {}

  def get(self,idx=0):
    return self.data.get(idx,'No Key')

  def push(self,ele):
    """
    Insert the elements at last
    """
    self.data[self.length] = ele
    self.length = self.length + 1
    return self.data[self.length-1]

  def pop(self, idx=-1):
    deletedEle = ''
    lastElement = self.data[self.length - 1] if self.length > 0 else ''
    if lastElement != '':
      deletedEle = lastElement if idx == -1 else self.data.get(idx,'')
      if deletedEle != '' and deletedEle != lastElement:
        for i in range(idx, self.length -1 ):
          self.data[i] = self.data[i+1]

      if deletedEle != '':
        del self.data[self.length - 1]
        self.length = self.length - 1   
    else: 
      print("List is empty")   
    return lastElement if lastElement else deletedEle
  
  def insert(self,ele,idx=0):
    """
    Insert the element at first
    O(n)
    0 1 2 3 4
    0 - prevEle
    1 - currEle
    2 - nextEle

    """
    if self.data.get(idx,'') != '' and idx != 0:
      currEle = ele
      for i in range(0 + idx,self.length + 1 ):
        nextEle = self.data.get(i,'')
        self.data[i] = currEle
        currEle = nextEle
      self.length = self.length + 1
    else:
      print("KeyError for {0}".format(idx))
    return self.data.get(idx,'No Key')



    
"""
obj1 = MyList()
print(obj1.pop())
print(obj1.get())
obj1.push(10)
obj1.push(20)
obj1.push(30)
obj1.push(30)
print(obj1.data)
print(obj1.length)
obj1.pop(1)
print(obj1.data)
print(obj1.length)
obj1.insert(-5, 1)
obj1.insert(-10, 3)
print(obj1.data)
print(obj1.length)
obj1.pop()
print(obj1.data)
print(obj1.length)
obj1.pop(3)
print(obj1.data)
print(obj1.length)
"""
