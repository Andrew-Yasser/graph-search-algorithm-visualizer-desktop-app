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
pathlist=[]


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



  # function to calculate the cost of the solution path
def CalcPathCost(edges,EdgesWeights, solpath):
    edgecosts = dict(zip(tuple(edges), EdgesWeights))
    edgecosts.values()
    cost = 0
    for i in range(len(solpath) - 1):
        cost += edgecosts.get((solpath[i], solpath[i + 1]))
    return cost


solpath, itnum = IDDLS(graph, 'a', ['j','G'], 4)  

print("the solution path is", solpath)
print("goal found at level number: ",itnum)
print("cost is", CalcPathCost(inputedges,edges_weights, solpath))
