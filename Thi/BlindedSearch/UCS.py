def popMinCost(arr):
  min = arr[0].get_cost()
  idx = 0
  for id, node in enumerate(arr):
    if node.get_cost() < min:
      min = node.get_cost()
      idx = id
  return arr.pop(idx)


def UCS(tree, initState, endState):
  frontier = []
  explored = []

  initNode = tree.get_node(initState)
  initNode.cost = 0;
  frontier.append(initNode);

  print("Frontier: ", [(node.get_data(), node.get_cost()) for node in frontier])

  while len(frontier) > 0:
    state = popMinCost(frontier)
    explored.append(state)

    print("Check: ", (state.get_data(), state.get_cost()))
    print("Neighbors: ", [node.get_data() for node in (state.childrens + state.parents)])
    print("-------------------------------------")

    if state.get_data() == endState:
      return True;
    
    for neighbor in (state.childrens + state.parents):
      if neighbor not in (frontier + explored):
        frontier.append(neighbor)
        weight = tree.get_edge_weight(state, neighbor)
        tree.update_cost(neighbor, state, weight)
      elif neighbor in frontier:
        weight = tree.get_edge_weight(state, neighbor)
        tree.update_cost(neighbor, state, weight)
      
    print("Frontier: ", [(node.get_data(), node.get_cost()) for node in frontier])
  
  return False

