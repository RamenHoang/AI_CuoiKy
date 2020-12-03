class Node:
    def __init__(self, data, cost=-1):
        self.data = data
        self.cost = cost
        self.g = 0
        self.f = 0
        self.parents = []
        self.childrens = []

    def get_data(self):
        return self.data

    def get_cost(self):
        return self.cost

    def get_parents(self):
        return self.parents

    def get_childrens(self):
        return self.childrens


class Tree:
    def __init__(self):
        self.nodes = []
        self.branches = []

    def is_contains(self, node):
        for aNode in self.nodes:
            if aNode.get_data() == node.get_data():
                return True
        return False

    def get_node(self, node_name):
        for node in self.nodes:
            if node.get_data() == node_name:
                return node
        return False

    def add_node(self, node_name):
        node = Node(node_name)
        if not self.is_contains(node):
            self.nodes.append(node)
        else: 
            del node
    
    def add_a_node(self, aNode):
        if not self.is_contains(aNode):
            self.nodes.append(aNode)

    def add_node_from(self, arr_of_node_name):
        for node_name in arr_of_node_name:
            new_node = Node(node_name)
            if self.is_contains(new_node) == False:
                self.nodes.append(new_node)
            else:
                del new_node
    
    def add_node_from_tuple(self, arr_of_node):
        for node_name, node_cost in arr_of_node:
            new_node = Node(node_name, node_cost)
            if self.is_contains(new_node) == False:
                self.nodes.append(new_node)
            else:
                del new_node

    def add_branch(self, start_node, end_node, weight=0):
        for branch in self.branches:
            if branch[0].get_data() == start_node.get_data() and branch[1].get_data() == end_node.get_data():
                if branch[2] != weight:
                    branch[2] = weight
                break
        
        _start_node = self.get_node(start_node.get_data()) or start_node
        _end_node = self.get_node(end_node.get_data()) or end_node

        self.add_a_node(_start_node)
        self.add_a_node(_end_node)

        new_branch = (_start_node, _end_node, weight)
        self.branches.append(new_branch)

        _start_node.get_childrens().append(_end_node)
        _end_node.get_parents().append(_start_node)
    
    def add_branch_from(self, arr_of_branch):
        for branch in arr_of_branch:
            start_node = Node(branch[0])
            end_node = Node(branch[1])
            self.add_branch(start_node, end_node, branch[2])
    
    def get_weight(self, start_node, end_node):
        for branch in self.branches:
            if (branch[0] == start_node and branch[1] == end_node) or (branch[0] == end_node and branch[1] == start_node):
                return branch[2]
        return 0

    def show_nodes(self):
        for node in self.nodes:
            print(node.get_data(), ' - ', node.get_cost())
    
    def show_branches(self):
        for branch in self.branches:
            print(branch[0].get_data(), ' - ', branch[1].get_data(), ' - ', branch[2])