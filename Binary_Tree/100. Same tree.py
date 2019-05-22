# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True

        if not p:
            return False

        if not q:
            return False

        if q.val != p.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


if __name__ == "__main__":
    q = TreeNode(1)
    q.left = TreeNode(2)
    q.right = TreeNode(3)
    p = TreeNode(1)
    p.left = TreeNode(3)
    p.right = TreeNode(2)
    assert Solution().isSameTree(q, p) == False
