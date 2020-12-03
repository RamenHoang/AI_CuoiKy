class Node:
  def __init__(self, data):
    super().__init__()
    self.data = data
    self.childrens = []
    self.parents = []
  
  def getData(self):
    return self.data

  def getChildrens(self):
    return self.childrens

  def getParents(self):
    return self.parents
  
  def isContainChild(self, _node):
    for node in self.childrens:
      if node.getData() == _node.getData():
        return True
    return False
  
  def isContainParent(self, _node):
    for node in self.parents:
      if node.getData() == _node.getData():
        return True
    return False
  
  def appendChild(self, node):
    if not self.isContainChild(node):
      self.childrens.append(node)
  
  def appendParent(self, node):
    if not self.isContainParent(node):
      self.parents.append(node)


class Graph:
  def __init__(self):
    self.nodes = []
    self.edges = []
  
  def nNode(self):
    return len(self.nodes)
  
  def nEdge(self):
    return len(self.edges)
  
  def isContain(self, nodeName):
    for node in self.nodes:
      if node.getData() == nodeName:
        return True
    return False

  def addNode(self, nodeName):
    self.nodes.append(Node(nodeName))

  def getNode(self, nodeName):
    for node in self.nodes:
      if node.getData() == nodeName:
        return node
    return None

  def addBranch(self, fromNode, toNode, weight=0):
    if not self.isContain(fromNode):
      self.addNode(fromNode)
    if not self.isContain(toNode):
      self.addNode(toNode)
    
    fNode = self.getNode(fromNode)
    tNode = self.getNode(toNode)

    edge = (fNode, tNode, weight)
    self.edges.append(edge)
    
    