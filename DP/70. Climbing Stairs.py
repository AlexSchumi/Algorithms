class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n or n == 0:
            return 0
        mem = {}
        return self.helper2(n, mem)
        #return self.helper(n,0) first implementation of climbing stairs

    """
    This is my first implementation of climbing stairs using recursion
    Time complexity: exponential time using recursion
    Space complexity: O(1)
    """

    def helper(self, n, cur):
        if cur > n:
            return 0
        if cur == n:
            return 1
        if cur < n:
            return self.helper(n, cur + 1) + self.helper(n, cur + 2)

    """
    This is my second implementation of climbing stairs
    Time complexity: O????? look at video for DP
    Space complexity: O(n)
    """
    def helper2(self, n, mem):
        if n in mem: # add this line for memorization
            return mem[n]
        if n <= 2:
            f = n
        if n > 2:
            f = self.helper2(n-1, mem) + self.helper2(n-2, mem)
            mem[n] = f
        return f

    """
    This is also recursion implementation using exponential Time
    """
    def climbStairs2(self, n):
        if n <= 2:
            return n
        else:
            return self.climbStairs2(n-1) + self.climbStairs2(n-2)

    """
    This is bottom-up dp algorithm using O(n) time
    """
    def climbStairs3(self, n):
        dp = [0 for _ in range(n)]
        dp[0] = 1
        dp[1] = 2
        
        for i in range(2,n):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n-1]

print(Solution().climbStairs3(30))
