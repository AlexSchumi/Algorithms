class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        queue = []
        queue.append((root,1))
        max_width = 1
        width = 1
        #cur_level = 0
        while queue:
            size = len(queue)
            width = queue[-1][1] - queue[0][1] + 1
            if width > max_width:
                max_width = width
            for i in range(size):
                node, val = queue.pop(0)
                if node.left:
                    queue.append((node.left, 2*(val-1) + 1))
                if node.right:
                    queue.append((node.right, 2*val))

            # update maximum width after popping up all nodes in one level
        return max_width
