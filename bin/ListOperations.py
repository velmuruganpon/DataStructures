class ListOperations:
  def __init__(self,xs:list):
    self.xs = xs

  def __repr__(self):
    return "created object for ListOperations in memory {0}".format(hex(id(self)))
  
  def push(self,ele):
    """
    add things at the end of the array/list

    """
    self.xs.append(ele)
  
  def pop(self, idx = -1):
    """
    delete the element from last or idx position from array

    """
    self.xs.pop(idx)
  
  def enQueue(self, ele, idx = 0):
    """
    insert the element in the front or any position

    """
    self.xs.insert(idx, ele)


