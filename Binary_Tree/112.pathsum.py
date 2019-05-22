class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# This version is BFS version of pathsum, which is more complicated;
def hasPathSum(root, sum):
    """
    :type root: TreeNode
    :type sum: int
    :rtype: bool
    """
    #if not root:
    #    return False
    res = []
    stack = [(root, 0)] #initialize stack
    while stack:
        node, val = stack.pop()
        if node.right:
            stack.append((node.right, val + node.val))
        if node.left:
            stack.append((node.left, val + node.val))
        if not node.left and not node.right: # if this is a leaf node in binary tree
            res.append(val + node.val)
    if sum in res:
        return True
    return False


# This will be my second version of haspathsum, which is a DFS version
def hasPathSum2(root, sum):
    """
    :type root: TreeNode
    :type sum: int
    :rtype: bool
    """
    return helper(root, sum)

def helper(root, res):
    if not root:
        return False
    if not root.left and not root.right: # if this will be a leaf node
        return res == root.val # check if root.val is equal to remaining value
    res = res-root.val # remaining value by deducting current node value
    if root.left:
        helper(root.left, res) # we pass the remaining value in the path
    if root.right:
        helper(root.right, res)
    return helper(root.left, res) or helper(root.right, res)

# build a tree in this step
root = TreeNode(5)
node1 = TreeNode(4)
node2 = TreeNode(8)
node3 = TreeNode(11)
node4 = TreeNode(13)
node5 = TreeNode(4)
node6 = TreeNode(7)
node7 = TreeNode(2)
node8 = TreeNode(1)
root.left = node1
root.right = node2
node1.left = node3
node3.left = node6
node3.right = node7
node2.left = node4
node2.right = node5
node5.right = node8
print(hasPathSum2(root, 22))
