# This script is to postorder traversal graph
def postorder(graph):
    marked = [False] * len(graph) # set marked for not repeating
    stack = []
    for node in graph:
        if marked[node] == False:
            dfs(graph, node, marked, stack)
    return stack

def dfs(graph, node, marked, stack):
    """
    :type node: graph node
    :type graph: List[List[int]]
    :type marked: boolean
    """
    marked[node] = True   # set marked n as True to make it traversed
    for n in graph[node]: # for every n in adj of node
        if not marked[n]:
            dfs(graph, n, marked, stack) # recursion for dfs traversal
    stack.append(node)

# The difference between preorder and postorder is that
# In preorder, we append the results before the stack has finished;
# While in postorder, we append the results when the stack has finished;

# one example for graph traversal;
graph = {0:[1],1:[0,2,4],2:[1,5],3:[4],4:[1,3,5],5:[2,4,6,8],6:[5,7],7:[6],8:[5]}

l = postorder(graph)
print(len(l))
print(l)
