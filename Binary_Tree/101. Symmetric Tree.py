# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    This is my DFS recursion implementation
    """
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        return self.isMirror(root.left, root.right)

    def isMirror(self, p, q):
        if not q and not p:
            return True
        if not q or not p:
            return False
        if q.val != p.val:
            return False
        return self.isMirror(p.left, q.right) and self.isMirror(p.right, q.left)

    """
    This is BFS implementation of symmetric Tree
    """
    def isSymmetric2(self, root):
        if not root:
            return True
        queue = []
        val = []
        queue.append(root)
        val.append(root.val)

        while queue:
            length = len(queue)
            if val != val[::-1]:
                return False
            val = []
            for i in range(length):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                    val.append(node.left.val)
                else:
                    val.append(0)

                if node.right:
                    queue.append(node.right)
                    val.append(node.right.val)
                else:
                    val.append(0)
        return True

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.right = TreeNode(4)
    root.left.left = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)
    assert Solution().isSymmetric(root) == True
