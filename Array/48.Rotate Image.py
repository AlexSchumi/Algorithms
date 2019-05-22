class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        """
        This is my implementation of clockwise rotate image
        Time complexity: O(n^2)
        Space complexity: O(1)
        """

        if not matrix or len(matrix) == 0:
            return

        pair = 0
        # swap the symmetry elements
        for i in range(len(matrix)):
            for j in range(len(matrix)-1, i, -1):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # reverse every row in matrix
        for i in range(len(matrix)):
            matrix[i] = matrix[i][::-1]

# for debug
image = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
print(Solution().rotate(image))
