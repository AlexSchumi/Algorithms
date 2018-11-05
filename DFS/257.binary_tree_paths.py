# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        paths = []
        if not root:
            return paths
        path = []
        self.dfs2(root, path, paths)
        return paths

    def dfs(self, root, path, paths):
        if not root:
            return
        if not root.left and not root.right:
            paths.append(path+str(root.val))
        #if root.left:
        self.dfs(root.left,  path + str(root.val)+'->', paths)
        #if root.right:
        self.dfs(root.right, path+str(root.val)+'->', paths)

    def dfs2(self, root, path, paths):
        if not root:
            return
        if not root.left and not root.right:
            #path = path.append(root.val)
            paths.append(path + [root.val])

        if root.left:
            #path = path.append(root.val)
            self.dfs2(root.left, path + [root.val], paths)

        if root.right:
            #path = path.append(root.val)
            self.dfs2(root.right, path + [root.val], paths)

"""
The anything I make mistake is that I have to do backtrack

Difference between path + [] and path.append()

extend, like many other list operations, operates in-place and returns None. ListA is modified with the extra elements.

If I use extend and .append in path, what I got is a none type results; If I use list + [], i will get a revised list
"""

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
print(Solution().binaryTreePaths(root))
