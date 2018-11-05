# two versions to traversal graph by dfs
def preorder(graph):
    marked = [False] * len(graph) # set marked for not repeating
    stack = []
    for node in graph:
        if not marked[node]:
            dfs2(graph, node, marked, stack) # careful with duplication
    return stack

def dfs(graph, node, marked, stack):
    """
    :type node: graph node
    :type graph: List[List[int]]
    :type marked: boolean
    """
    if not marked[node]:
        marked[node] = True  # set marked n as True to make it traversed
        stack.append(node)
        for n in graph[node]: # for every n in adj of node
            dfs(graph, n, marked, stack) # recursion for

def dfs2(graph, node, marked, stack):
    """
    :type node: graph node
    :type graph: List[List[int]]
    :type marked: boolean
    """
    stack.append(node)
    marked[node] = True  # set marked n as True to make it traversed
    for n in graph[node]: # for every n in adj of node
        if not marked[n]:
            dfs2(graph, n, marked, stack) # recursion for

graph = {0:[1],1:[0,2,4],2:[1,5],3:[4],4:[1,3,5],5:[2,4,6,8],6:[5,7],7:[6],8:[5]}

l1 = preorder(graph)

print(len(l1))
print(l1)
