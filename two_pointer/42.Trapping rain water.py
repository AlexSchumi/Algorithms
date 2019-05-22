class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        """
        Time complexity: O(n)
        Space complexity: O(n)
        """

        if not height or len(height) == 0:
            return 0
        leftmost = [0] * len(height)
        rightmost = [0] * len(height)
        res = 0
        leftmax = 0
        rightmax = 0

        for i in range(len(height)):
            if height[i] > leftmax:
                leftmost[i] = leftmax = height[i]
            else:
                leftmost[i] = leftmax

        for i in range(len(height)-1, -1, -1):
            if height[i] > rightmax:
                rightmost[i] = rightmax = height[i]
            else:
                rightmost[i] = rightmax
                

        for i in range(len(height)):
            if height[i] - min(leftmost[i], rightmost[i]) < 0:
                res += min(leftmost[i], rightmost[i]) - height[i]
        return res
