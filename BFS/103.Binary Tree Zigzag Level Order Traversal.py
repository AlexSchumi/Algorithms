# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    """
    This is my implementation of zigzaglevelorder by bfs
    Time complexity:
    Space complexity:
    """
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ress = []
        if not root:
            return ress

        queue = []
        queue.append(root)
        cur_level = 1
        while(queue):
            size = len(queue)
            res = []
            for i in range(size):
                node = queue.pop(0)
                res.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if cur_level % 2 == 0:
                res = res[::-1]

            cur_level += 1
            ress.append(res)
        return ress

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(Solution().zigzagLevelOrder(root))
