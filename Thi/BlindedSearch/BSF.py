def BFS(graph, initState, endState):
  frontier = []
  explored = []
  
  frontier.append(initState)
  print("Frontier: ", frontier)
  
  while len(frontier) > 0:
    state = frontier.pop(0)
    explored.append(state)

    print("Check: ", state)
    print("--------------------------------")
    if endState == state:
      return True
    
    for neighbor in graph.neighbors(state):
      if neighbor not in (frontier + explored):
        frontier.append(neighbor)
    
    print("Frontier: ", frontier)
    
    
  return False
