import sys

class HashTable:
  def __init__(self):
    """
    data : [
       [ [1, 'vel'] ] ,  
       [ [2, 'abi'] ], 
       [ [3, 'raj'] , [ 4, 'vedha'] ] 
       ]

    Element :  print(data[2])
     [ [3, 'raj'] , [ 4, 'vedha'] ] ]

     length of Element : 2

     access the element :

     key  = Element[0][0], Element[1][0]
     value = Element[0][1], Element[1][1]

    """

    self.size = 100
    self.data = [ [] for i in range(self.size) ]
  
  def __str__(self):
    return str(self.__dict__)
  
  def hash(self, key):
    return len(key) % self.size
   
  def getLength(self, xs):
    return len(xs)
 
  def ifKeyValueInEle(self, chkEle, ele, key):
    if chkEle:
      lenEle = self.getLength(ele)
      for i in range(lenEle):
        if ele[i][0] == key:
          print("Key - {0} already exists".format(key))
          return True, ele[i][1]
        else:
          return False, None
    else:
      return False, None

  def set(self, key, value):
    hashId = self.hash(str(key))
    ele = self.data[hashId]
    print(ele)
    chkEle = True if ele else False
    chkKeyInEle, val = self.ifKeyValueInEle(chkEle, ele, key)
    if chkKeyInEle:
      sys.exit(-1)
    else:
      ele.append([key, value])

  def get(self,key):
    hashId = self.hash(str(key))
    ele = self.data[hashId]
    chkEle = True if ele else False
    chkKeyInEle, val = self.ifKeyValueInEle(chkEle, ele, key)
    return val if chkKeyInEle else None

      

obj1 = HashTable()
obj1.set(1,'vel')
obj1.set(2,'abi')
obj1.set(3,'raj')
obj1.set(103,'vedha')

a = obj1.get(4)
b = obj1.get(103)

print(a)
print(b)

print(obj1)
