from Graph import Node, Tree
from GreedyFirstSearch import GFS
from AStarFirstSearch import ASFS

nodes_name = [('A', 20), ('B', 0), ('C', 15), ('D', 6), ('E', 7), ('F', 10),
              ('G', 5), ('H', 3), ('I', 8), ('K', 12)]
branches = [('A', 'C', 3), ('A', 'D', 5), ('A', 'E', 1), ('C', 'F', 9),
            ('D', 'F', 5), ('D', 'I', 4), ('E', 'G', 2), ('E', 'K', 1),
            ('F', 'B', 6), ('I', 'B', 8), ('I', 'G', 8), ('G', 'B', 3),
            ('G', 'H', 1), ('H', 'B', 5)]

tree = Tree()
tree.add_node_from_tuple(nodes_name)
tree.add_branch_from(branches)

# tree.show_nodes()

# print('------------------------')

# tree.show_branches()
print('Greedy First Search')
GFS(tree, 'A', 'B')
print('============================================================')
print('A Star First Search')
ASFS(tree, 'A', 'B')
