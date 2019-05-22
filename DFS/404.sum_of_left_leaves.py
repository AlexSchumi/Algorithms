# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        res = 0
        if root.left and root.left.left is None and root.left.right is None: # if we have left leave node
            res += root.left.val

        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right) + res

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(Solution().sumOfLeftLeaves(root))
