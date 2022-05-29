#a Class enclosing all graph attributes
class Graph:

    # Different attributes of a graph
    graph = dict()      # the graph in the form of dictionary
    InitialNode=" "     # the starting nodes where the search in graph starts from
    GoalNodes=[]         # the goal(s), can have multiple or single node as the goal
    Nodes = []          # the list of graph nodes, used as an input confirmation to the nodes in the dictionary
    EdgesWeights = []   # the list containing each edge cost, entered with the same order of edges from the dictionary
    MaxDepth = 0        # the maximum depth used for the depth limited searching algorithm
    iterat=0            # the number of iteration used in iterative deepning
    edges=[]            # the list of edges in the input graph, automatically set by the input dictionary using a function in Logic
    dir= False          # the field used to know if graph is directed or not
    path = []       # the solution path of the graph using any algorithm will be stored here
    visited = []   # the visited nodes of the graph, in order, while trying to get solution path using any algorithm will be stored here
