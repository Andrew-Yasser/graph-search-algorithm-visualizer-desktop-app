import json #Json built function that reads the string input and transform it into dictionary

# two global values used to set the heuristic function in case of Greedy or A* search
HeuristicFunctionAstar= dict()
HeuristicFunctionGreedy= dict()

#an empty list used in depth limited and iterative deepning search
pathlist= []

# function to calculate the cost of the solution path
def CalcPathCost(edges,EdgesWeights, solpath):
    edgecosts = dict(zip(tuple(edges), EdgesWeights))
    edgecosts.values()
    cost = 0
    for i in range(len(solpath) - 1):
        cost += edgecosts.get((solpath[i], solpath[i + 1]))
    return cost

# function to get the edges to be highlighted in solution drawing
def GetHighlightedEdges(solpath):
    highlighted_edges = []
    for i in range(len(solpath) - 1):
        highlighted_edges.append((solpath[i], solpath[i + 1]))
    return highlighted_edges


# function that converts string od graph dictionary into dictionary
def getGraph(string):
    res = json.loads(string)
    return (res)



# function to get edges from the dictionary, return ['A', 'B'],['A', 'C'],['B', 'D']
def getEdgesList(dict):
    edges = []
    for key, values in dict.items():
        for i in values:
            edges.append((key, i))
    return edges


# function to get list of nodes from string
def getNodesList(string):
    li = list(string.split(" "))
    return li


#function to get list of weights of edges from string
def getWeightsList(str):
    a_list = str.split()
    map_object = map(int, a_list)
    weightslist = list(map_object)
    return weightslist


#function to calculate path cost for Greedy search
def CalculateSolutionCost(SolutionPath, HeuristicFunction):
  cost=0
  for key in HeuristicFunction:
    if key in SolutionPath:
      cost += HeuristicFunction[key]
  return cost


#Function to seperate solution path from each node cost
def GetSolutionPathAsList(SolutionPath):
  list=[item[0] for item in SolutionPath]
  return list


def DFS(graph,InitialNode, GoalNode):
    visited=[]
    stack= [[InitialNode]]
    while stack:
        # get the first element
        path = stack.pop()
        # get the last node from the path
        node=path[-1]
        #check if the node is already visited, if yes continue
        if node in visited:
            continue
        visited.append(node)
        # if a path found to have a goal node, return it with the visited list
        if node in GoalNode:
            return path,visited
        else:
            # reversing the order of the adjacent nodes
            adjacent_nodes=graph.get(node,[]).__reversed__()
            for node_2 in adjacent_nodes:
                new_path= path.copy()
                new_path.append(node_2)
                stack.append(new_path)



def BFS(graph, InitialNode, GoalNode):
    visited = []
    visited.append(InitialNode)
    # maintain a queue of paths
    queue = []
    # push the first node into the queue
    queue.append([InitialNode])
    while queue:
        # get the first path from the queue of paths
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        # if a path found to have a goal node, return it with the visited list
        if node in GoalNode:
            return path, visited
        # enumerate all adjacent nodes, construct a new path and push it into the queue
        for adjacent in graph.get(node, []):
            if (visited[-1] not in GoalNode):
                visited.append(adjacent)
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)



def DLS(graph, start, goal, path, level, maxD):
    # if the node is not in the path already append it, to prevent repeating
    if start not in path:
        path.append(start)
    # if the node in the goal list return the current path
    if start in goal:
        return path
    #if the current level is the maximum level specified return nothing
    if level == maxD:
        return False
    for child in graph[start]:
        #recursive calls for the DLS function
        if DLS(graph, child, goal, path, level + 1, maxD):
            return path
        path.pop()
    return False




def IDDLS(graph, start, goal, max_depth):
    # iterate depth-limit search till the maximum specified depth to get shallowest path.
    for iterat in range(0, max_depth+1):
        result = DLS(graph, start, goal, pathlist, 0, iterat) #calls the depth limited function with the iteration as the max level
        # if result if found and not false bring it with the level it is found at
        if (result):
            return result, iterat
    return False, False


#Function to add the cost of each edges in graph dictionary
def BuildDictWithCost (nodes, graphdict, edges_weights):
    OriginalValues=[]
    ListofTupleValues=[]
    NewVals = []
    FlatOriginalValues = []
    SizeofValuesofkey = []
    for key, val in graphdict.items():
         OriginalValues.append(val)
    for sublist in OriginalValues:
        for item in sublist:
            FlatOriginalValues.append(item)
    for i in range(len(FlatOriginalValues)):
        ListofTupleValues.append((FlatOriginalValues[i],edges_weights[i]))
    for key, val in graphdict.items():
        SizeofValuesofkey.append(len(graphdict[key]))
    for number in SizeofValuesofkey:
        vals = []
        for i in range(number):
            if len(ListofTupleValues):
                vals.append(ListofTupleValues.pop(0))
        if len(vals):
            NewVals.append(vals)
    newgraph = dict(zip(nodes, NewVals))
    return newgraph




#Function to calculate the total path cost
def PathCost(path):
  TotalCost = 0
  #Iterate over each node and its cost within the path
  #Ex (node, cost) = ('A', 2)
  for (node, cost) in path:
    TotalCost += cost
   #The second return is to break the tie alphabetically
   #in case of equal TotalCost (Based on alphabetic order of last node in path)
   #[0] is used to return the node only without its cost
  return TotalCost, path[-1][0]

def UniCost(graph, StartNode, GoalNode):
  visited = []
  PriorityQueue = [[(StartNode, 0)]]
  while PriorityQueue:
    #Sort the paths in the priority queue based on their cost
    PriorityQueue.sort(key=PathCost)
    #Choose the path with least cost
    path = PriorityQueue.pop(0)
    node = path[-1][0]
    #Check whether the last node in the path have been visited
    #If it was already visited we'll skip it
    if node in visited:
      continue
    visited.append(node)
    if node in GoalNode:
      return path, visited
    else:
      #AdjacentNodes are the children of the current node
      AdjacentNodes = graph.get(node, [])
      for (node2, cost) in AdjacentNodes:
        NewPath = path.copy()
        NewPath.append([node2, cost])
        PriorityQueue.append(NewPath)



def PathHCost(path):
  LastNode = path[-1][0]
  #HCost (h(n) function) represents the estimated cost from current node n to goal
  #This is the heuristic function
  HCost = HeuristicFunctionGreedy[LastNode]
  return HCost, LastNode


def Greedy(graph, StartNode, GoalNode):
  visited = []
  PriorityQueue = [[[StartNode, 0]]]
  while PriorityQueue:
    #Sort the paths in the priority queue based on their PathHCost
    PriorityQueue.sort(key=PathHCost)
    #Choose the path with least H cost
    path = PriorityQueue.pop(0)
    node = path[-1][0]
    #Check whether the last node in the path have been visited
    #If it was already visited we'll skip it
    if node in visited:
      continue
    visited.append(node)
    if node in GoalNode:
      return path, visited
    else:
      #AdjacentNodes are the children of the current node
      AdjacentNodes = graph.get(node, [])
      for (node2, cost) in AdjacentNodes:
        NewPath = path.copy()
        NewPath.append([node2, cost])
        PriorityQueue.append(NewPath)






def PathFCost(path):
  #GCost (g(n) function) represents the actual cost to current node n
  #This is the uniform cost search
  GCost = 0
  for (node, cost) in path:
    GCost += cost
  LastNode = path[-1][0]
  #HCost (h(n) function) represents the estimated cost from current node n to goal
  #This is the heuristic function
  HCost = HeuristicFunctionAstar[LastNode]
  #FCost is a function that combines the 2 previous costs into a final cost
  #f(n)=g(n)+h(n)
  FCost = GCost + HCost
  return FCost, LastNode


def AStar(graph, StartNode, GoalNode):
  visited = []
  PriorityQueue = [[(StartNode, 0)]]
  while PriorityQueue:
    #Sort the paths in the priority queue based on their PathFCost
    PriorityQueue.sort(key=PathFCost)
    #Choose the path with least F cost
    path = PriorityQueue.pop(0)
    node = path[-1][0]
    #Check whether the last node in the path have been visited
    #If it was already visited we'll skip it
    if node in visited:
      continue
    visited.append(node)
    if node in GoalNode:
      return path, visited
    else:
      #AdjacentNodes are the children of the current node
      AdjacentNodes = graph.get(node, [])
      for (node2, cost) in AdjacentNodes:
        NewPath = path.copy()
        NewPath.append([node2, cost])
        PriorityQueue.append(NewPath)