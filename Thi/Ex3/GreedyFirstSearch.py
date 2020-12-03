def pop_min(arr):
    min = arr[0].get_cost()
    idx = 0
    for id, el in enumerate(arr):
        if min > el.get_cost():
            min = el.get_cost()
            idx = id
    
    return arr.pop(idx)


def GFS(tree, start_node, end_node):
    frontier = []
    explored = []

    frontier.append(tree.get_node(start_node))
    print('Frontier: ', [(node.get_data(), node.get_cost()) for node in frontier])
    print('Exlored: ', [(node.get_data(), node.get_cost()) for node in explored])
    while len(frontier) > 0:
        current_node = pop_min(frontier)
        explored.append(current_node)
        print('Checked node: ', (current_node.get_data(), current_node.get_cost()))
        print('--------------------------------------------------------------------')
        if (current_node.get_data() == end_node):
            return True
        
        for neighbor in (current_node.get_parents() + current_node.get_childrens()):
            if neighbor not in (frontier + explored):
                frontier.append(neighbor)

        print('Frontier: ', [(node.get_data(), node.get_cost()) for node in frontier])
        print('Explored: ', [(node.get_data(), node.get_cost()) for node in explored])
    return False