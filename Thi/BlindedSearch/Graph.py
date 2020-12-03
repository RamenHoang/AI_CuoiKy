class Node:
  def __init__(self, data, cost = -1):
    self.data = data
    self.parents = []
    self.childrens = []
    self.cost = cost

  def get_data(self):
    return self.data

  def get_cost(self):
    return self.cost

  def get_children(self):
    return self.childrens

  def get_parents(self):
    return self.parents


class Tree:
  def __init__(self):
    self.nodes = []
    self.edges = []

  def clear(self):
    self.nodes = []
    self.edges = []

  def number_of_nodes(self):
    return len(self.nodes)

  def number_of_edges(self):
    return len(self.edges)

  def get_index(self, node):
    for idx, n in enumerate(self.nodes):
      if n.get_data() == node.get_data():
        return idx
    return -1
  
  def get_node(self, node_data):
    for node in self.nodes:
      if (node.get_data() == node_data):
        return node
    
    return -1;
  
  def get_edge_weight(self, startNode, endNode):
    for edge in self.edges:
      if (edge[0] == startNode and edge[1] == endNode) or (edge[1] == startNode and edge[0] == endNode):
        return edge[2]
    
    return -1

  def add_node(self, node_name):
    node = Node(node_name)
    if not self.is_contain(node):
      self.nodes.append(node)

  def add_node_from(self, array_of_nodes_name):
    for el in array_of_nodes_name:
      node = Node(el)
      if not self.is_contain(node):
        self.nodes.append(node)

  def is_contain(self, node):
    for el in self.nodes:
      if el.get_data() == node.get_data():
        return True
    return False

  def add_edge(self, start_name, end_name, weight):
    start_node = Node(start_name)
    end_node = Node(end_name)
    if not self.is_contain(start_node):
      self.add_node(start_name)
    if not self.is_contain(end_node):
      self.add_node(end_name)
    start_index = self.get_index(start_node)
    end_index = self.get_index(end_node)
    self.nodes[start_index].childrens.append(self.nodes[end_index])
    self.nodes[end_index].parents.append(self.nodes[start_index])
    self.edges.append((self.nodes[start_index], self.nodes[end_index], weight))

  def add_edges_from(self, array_of_tuple_node):
    for tup in array_of_tuple_node:
      start = tup[0]
      end = tup[1]
      weight = tup[2]
      self.add_edge(start, end, weight)

  def update_cost(self, targetNode, parentNode, edge_weight):
    if targetNode.get_cost() == -1 or targetNode.get_cost() > parentNode.get_cost() + edge_weight:
      targetNode.cost = parentNode.get_cost() + edge_weight
    

