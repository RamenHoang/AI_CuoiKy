import networkx as nx
from BSF import BFS
from DFS import DFS
from UCS import UCS
from Graph import Tree

nodes = ["S", "A", "B", "C", "D", "E", "F", "G", "H"]
weigthed_edge = [
  ("S", "A", 3),
  ("S", "B", 6),
  ("S", "C", 2),
  ("A", "D", 3),
  ("B", "D", 4),
  ("B", "G", 9),
  ("B", "E", 2),
  ("C", "E", 1),
  ("D", "F", 5),
  ("E", "H", 5),
  ("F", "E", 6),
  ("H", "G", 8),
  ("F", "G", 5)
]

myGraph = nx.Graph()
myGraph.add_nodes_from(nodes)
myGraph.add_weighted_edges_from(weigthed_edge)

startNode = "S"
endNode = "G"

def printResult(endNode, result):
  if result == True:
    print("=> ", endNode, " node founded")
  else:
    print("=> ", endNode, " node not founded")


# --------------------------------------------------------
print(">>BFS")
resBFS = BFS(myGraph, startNode, endNode)
printResult(endNode, resBFS);

# --------------------------------------------------------
print("\n\n")
print(">>DFS")
resDFS = DFS(myGraph, startNode, endNode)
printResult(endNode, resDFS)

# ----------------------------------------------------------
print("\n\n")
print(">>UCS")
myTree = Tree()
myTree.add_node_from(nodes)
myTree.add_edges_from(weigthed_edge)
resUCS = UCS(myTree, startNode, endNode)
printResult(endNode, resUCS)



