import sys
class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        Can only go down or right
        """

        """
        This is top-down algorithm using DP
        Time complexity: O(mn)
        Space complexity: O(mn)
        """
        if not grid or len(grid) == 0:
            return 0
        m = len(grid)
        n = len(grid[0])
        dp = [[0] * len(grid[0]) for _ in range(len(grid))] # create a dp matrix to store minimum path
        sum = 0

        for j in range(len(grid[0])):
            sum += grid[0][j]
            dp[0][j] = sum
        sum = 0
        for j in range(len(grid)):
            sum += grid[j][0]
            dp[j][0] = sum

        #if m > 1 or n > 1:
        self.dfs(grid, m-1, n-1, dp)
        return dp[m-1][n-1]

    def dfs(self, grid, i, j, dp):
        m = len(grid)
        n = len(grid[0])
        if i < 0 or j < 0 or i >= m or j >= n:
            #return sys.maxsize
            return
        if i == 0 or j == 0:
            return dp[i][j]

        if dp[i][j] != 0: # if dp of this cell is known
            return dp[i][j]

        res = min(self.dfs(grid, i-1, j, dp), self.dfs(grid, i, j-1, dp)) + grid[i][j]
        dp[i][j] = res
        return res

    """
    This is bottom-up algorithm using DP
    Time complexity: O(mn)
    Space complexity: O(mn)
    """
    def minPathSum2(self, grid):
        if not grid or len(grid) == 0:
            return 0
        m = len(grid)
        n = len(grid[0])
        dp = [[0] * len(grid[0]) for _ in range(len(grid))] # create a dp matrix to store minimum path
        sum = 0

        for j in range(len(grid[0])):
            sum += grid[0][j]
            dp[0][j] = sum
        sum = 0
        for j in range(len(grid)):
            sum += grid[j][0]
            dp[j][0] = sum

        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[m-1][n-1]


if __name__ == "__main__":
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    #grid = [[1,2,5],[3,2,1]]
    print(Solution().minPathSum2(grid))
    assert Solution().minPathSum2(grid) == 7
