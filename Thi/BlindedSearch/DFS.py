def DFS(graph, initState, endState):
  frontier = []
  exploser = []

  frontier.append(initState)
  print("Frontier: ", frontier)
  while len(frontier) > 0:
    state = frontier.pop()
    exploser.append(state)

    print("Check: ", state)
    print("--------------------------------")

    if state == endState:
      return True
    
    for neighbor in graph.neighbors(state):
      if neighbor not in (frontier + exploser):
        frontier.append(neighbor)
    
    print("Frontier: ", frontier)
  
  return False