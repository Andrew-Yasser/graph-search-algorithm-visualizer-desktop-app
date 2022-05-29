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
  PriorityQueue = [[[StartNode, 0]]]
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
    
    
# function to calculate the cost of the solution path
def CalcPathCost(edges,EdgesWeights, solpath):
    edgecosts = dict(zip(tuple(edges), EdgesWeights))
    edgecosts.values()
    cost = 0
    for i in range(len(solpath) - 1):
        cost += edgecosts.get((solpath[i], solpath[i + 1]))
    return cost
        
f= BuildDictWithCost(Nodes,graph,edges_weights)
solpath,visited= UniCost(f,"a",["G","j"])

print("the solution path is", solpath)
print("the visited nodes are",visited)
print("cost is", CalcPathCost(inputedges,edges_weights, solpath))

