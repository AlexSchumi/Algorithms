class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ress = []
        if not root:
            return res
        queue = []
        queue.append(root)

        while queue:
            res = []
            size = len(queue)
            for i in range(size):
                node = queue.pop(0)
                res.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            ress.append(res)
        return ress[::-1]

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(Solution().levelOrderBottom(root))
