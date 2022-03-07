class Graph:
  def __init__(self):
    self.vertexCount = 0
    self.adjacentList = {}

  def addVertex(self, vertex):
    self.adjacentList[vertex] = []
    self.vertexCount += 1

  def addEdge(self, vertex1, vertex2):
    self.adjacentList[vertex1].append(vertex2)
    self.adjacentList[vertex2].append(vertex1)

  def printGraph(self):
    for i in self.adjacentList.keys():
      print("{0} --> {1}".format(i, self.adjacentList[i]))


obj1 = Graph()
obj1.addVertex(vertex=0)  
obj1.addVertex(vertex=1)  
obj1.addVertex(vertex=2)  

obj1.addEdge(0,1)
obj1.addEdge(0,2)
obj1.addEdge(1,2)

obj1.printGraph()
 
    
    
    

