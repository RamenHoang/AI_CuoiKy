def pop_min(arr):
    min = arr[0].f
    idx = 0
    for id, el in enumerate(arr):
        if min > el.f:
            min = el.f
            idx = id
    
    return arr.pop(idx)

def ASFS(tree, start_node, end_node):
    frontier = []
    explored = []

    frontier.append(tree.get_node(start_node))
    print('Frontier: ', [(node.get_data(), node.f) for node in frontier])
    print('Explored: ', [(node.get_data(), node.f) for node in explored])
    while len(frontier) > 0:
        current_node = pop_min(frontier)
        explored.append(current_node)
        print('Checked node: ', (current_node.get_data(), current_node.f))
        print('--------------------------------------------------------------------')
        if (current_node.get_data() == end_node):
            return True
        
        for neighbor in (current_node.get_parents() + current_node.get_childrens()):
            if neighbor not in (frontier + explored):
                frontier.append(neighbor)
                neighbor.g = current_node.g + tree.get_weight(current_node, neighbor)
                neighbor.f = neighbor.g + neighbor.get_cost()
            elif neighbor in frontier:
                neighbor.g = current_node.g + tree.get_weight(current_node, neighbor)
                neighbor.f = neighbor.g + neighbor.get_cost()

        print('Frontier: ', [(node.get_data(), node.f) for node in frontier])
        print('Explored: ', [(node.get_data(), node.f) for node in explored])
    return False