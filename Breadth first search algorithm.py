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
            
  # function to calculate the cost of the solution path
def CalcPathCost(edges,EdgesWeights, solpath):
    edgecosts = dict(zip(tuple(edges), EdgesWeights))
    edgecosts.values()
    cost = 0
    for i in range(len(solpath) - 1):
        cost += edgecosts.get((solpath[i], solpath[i + 1]))
    return cost
            
            
solpath, visitednodes = BFS(graph, 'a', ['j','G'])


print("the solution path is", solpath)
print("the visited nodes are",visitednodes)
print("cost is", CalcPathCost(inputedges,edges_weights, solpath))


