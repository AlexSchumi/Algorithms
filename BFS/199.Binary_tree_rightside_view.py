class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # This is my implementation of binary tree right side view
    # I will use BFS to implement it
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root:
            return res

        queue = []
        queue.append(root)
        cnt = 1 # denotes how many nodes in the tree level
        pop_cnt = 0
        while queue:
            #if len(queue) == 1: # if we have the length is one, which means we have last node in this level
            node = queue.pop(0) # pop the queue from the left
            if (cnt - pop_cnt) == 1:
                res.append(node.val)
            pop_cnt += 1

            if tmp.left:
                cnt += 1
                queue.append(node.left)
            if tmp.right:
                cnt += 1
                queue.append(node.right)

        return res
"""
Think about how to impose level information in tree level traversal
"""
