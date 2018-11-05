# This is my implementation of valid binary search tree
import sys
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        minimum = -sys.maxsize-1
        maximum = sys.maxsize
        return self.helper(root, maximum, minimum)


    def helper(self, root, maximum, minimum):
        if not root:
            return True # exit for recursion

        if root.val >= maximum:
            return False
        if root.val <= minimum:
            return False

        return self.helper(root.left, min(root.val, maximum), minimum) and self.helper(root.right, maximum, max(root.val, minimum))
        # update minimum in right subtree
        # update maximum in left subtree

    def isValidBST2(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        res = self.helper2(root)
        if len(res) != len(set(res)):
            return False
        return sorted(res) == res

    def helper2(self, root):
        res = []
        if not root:
            return res
        res += self.helper2(root.left)
        res.append(root.val)
        res += self.helper2(root.right)
        return res

    # This is wrong version for recursion # revise it please
    def helper3(self, root, res):
        res = []
        if not root:
            return []
        res += self.helper3(root.left, res)
        res.append(root.val)
        res += self.helper3(root.right, res)


root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.right.left = TreeNode(3)
root.right.right = TreeNode(6)
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
# print(root.val)
res = []
print(Solution().helper3(root, res))
