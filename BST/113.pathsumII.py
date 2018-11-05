# This is my second implementation of pathsum using DFS

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root, obj):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        paths = []
        path = []
        if not root:
            return paths

        self.helper(root, path, paths, obj)
        return paths

    # This is a helper function to record the all path
    def helper(self, root, path, paths, obj):
        if not root:  # when we do not have nodes
            return

        if not root.left and not root.right: # if this will be a leaf node
            path = path + [root.val]
            if sum(path) == obj:
                # append the path into current path
                paths.append(path)     # append the path to the output

        #if root.left: # We can not use in this way, since we are always appending elements to path, we are changing path all
        #The time. We are kind of losing backtracking property in DFS;
        #path.append(root.val)
        #print(path)
        self.helper(root.left, path + [root.val], paths, obj)  # left subtree search
        #if root.right:
        self.helper(root.right, path + [root.val], paths, obj) # right subtree search

"""
The anything I make mistake is that I have to do backtrack

Difference between path + [] and path.append()

extend, like many other list operations, operates in-place and returns None. ListA is modified with the extra elements.

If I use extend and .append to updateing path, what I got is a none type results; If I use list + [], i will get a revised list
"""

"""
We only pass current list to the recursion function. Using list.append() will cause problems since we are changing it gloablly;
"""
#build a tree in this step
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
print(Solution().pathSum(root, 22))
