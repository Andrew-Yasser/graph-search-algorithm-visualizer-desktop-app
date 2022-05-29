graph = { "a" : ["b","c"],
          "b" : ["e", "f"],
          "c" : ["G", "H"],
          "e" : ["i"],
          "f" : ["j"],
          "G" : ["K"],
		  "H" : ["l"],
		  "i" : [],
		  "j" : [],
		  "K" : [],
		  "l" : [],
        }
inputedges= [('a', 'b'), ('a', 'c'), ('b', 'e'), ('b', 'f'), ('c', 'G'), ('c', 'H'), ('e', 'i'), ('f', 'j'), ('G', 'K'), ('H', 'l')]

edges_weights=[1,6,9,6,9,2,7,3,4,10]
Nodes= ["a","b","c","e","f","G","H","i","j","K","l"]


HeuristicFunctionAstar = {
    "a": 7,
    "b": 6,
    "c": 4,
    "e": 2,
    "f": 5,
    "G": 0,
    "H": 2,
    "i": 1,
    "j": 0,
    "l": 3,
    "K": 3
}

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
    
#Function to seperate solution path from each node cost
def GetSolutionPathAsList(SolutionPath):
  list=[item[0] for item in SolutionPath]
  return list

#function to calculate path cost for Greedy search
def CalculateSolutionCost(SolutionPath, HeuristicFunction):
  cost=0
  for key in HeuristicFunction:
    if key in SolutionPath:
      cost += HeuristicFunction[key]
  return cost

f= BuildDictWithCost(Nodes,graph,edges_weights)
p,visited= AStar(f,"a",["G","j"])
solpath = GetSolutionPathAsList(p)
c = PathFCost(p)[0]

print("the solution path is", solpath)
print("the visited nodes are",visited)
print("cost is", c)
