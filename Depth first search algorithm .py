
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
                
solpath, visitednodes = DFS(graph, 'a', ['j','G'])         
                
def CalcPathCost(inputedges,edges_weights):
    weights= dict(zip(inputedges, edges_weights))
    #print(weights)
    cost=0
    for i in range(len(solpath)-1):
        cost+= weights.get((solpath[i],solpath[i+1]))
    return cost
    path = []



print("the solution path is", solpath)
print("the visited nodes are",visitednodes)
print("cost is", CalcPathCost(inputedges,edges_weights))
