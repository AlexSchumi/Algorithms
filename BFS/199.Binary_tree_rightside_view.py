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

        while queue:
            size = len(queue)
            for i in range(size): # for this level's node
                node = queue.pop(0) # pop the queue from the left
                if i == size - 1: # we have finished traversal for this level
                    res.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res


"""
Think about how to impose level information in tree level traversal
add a variable size, which equal to the length of node in one level

a loop for the level
"""

"""
Time complexity: O(n)  since we traverse every node one by one
space complexity: O(n)
"""

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
root.left.right.left = TreeNode(8)
print(Solution().rightSideView(root))
