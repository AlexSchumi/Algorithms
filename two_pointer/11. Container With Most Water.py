class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        """
        My first implementation of algorithm TLE(using two pointer to optimize it)!!!
        Time complexity: O(n^2)
        Space complexity: O(1)
        """
        if not height or len(height) == 0:
            return 0
        res = 0

        for i in range(len(height)):
            for j in range(len(height)-1, i, -1):
                area = min(height[i],height[j]) * (j-i)
                res = max(res, area)
        return res

    def maxArea2(self, height):
        """
        Using two pointer to optimize algorithm!!! Good solution
        Time complexity: O(n)
        Space complexity: O(1)
        """
        i = 0
        j = len(height) - 1
        res = 0
        while(i < j):
            area = min(height[i], height[j])*(j-i)
            res = max(area, res)
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
        return res
