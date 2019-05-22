class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        """
        Second try with memorization(DP) successs (Top-down algorithm)
        Time complexity: O(mn)
        Space complexity: O(mn)
        """
        #used = [[0] * n for i in range(m)]
        dp = [[0] * n for i in range(m)]
        dp[0] = [1] * n
        for i in range(m):
            dp[i][0] = 1
        return self.dfs(m, n, m-1, n-1, dp)

    def dfs(self, m, n, i, j, dp):
        if i < 0 or j < 0 or i >= m or j >= n:
            return 0
        if dp[i][j] != 0:
            return dp[i][j]
            
        steps = self.dfs(m, n, i-1, j, dp) + self.dfs(m, n, i, j-1, dp)
        dp[i][j] = steps
        return steps

    """
    This is my try to use bottom up algorithm for uniquepath
    Time complexity: O(mn)
    Space complexity: O(mn)
    """
    def uniquePaths2(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0] * n for i in range(m)]
        dp[0] = [1] * n
        for i in range(m):
            dp[i][0] = 1

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]

    """
    First implementation without memorization, only with recursion: TLE!!!!
    With memory, success!!!
    """
    def uniquePaths3(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        #used = [[0] * n for i in range(m)]
        return self.dfs2(m, n, m-1, n-1)

    def dfs2(self, m, n, i, j):
        if i < 0 or j < 0 or i >= m or j >= n:
            return 0
        if i == 0 or j == 0:
            return 1
        #if used[i][j] == 1:
        #    return 0
        #used[i][j] = 1
        steps = self.dfs2(m, n, i-1, j) + self.dfs2(m, n, i, j-1)
        return steps

if __name__ == "__main__":
    print(Solution().uniquePaths2(2,10))
    #assert Solution().uniquePaths3(7,3) == 28
