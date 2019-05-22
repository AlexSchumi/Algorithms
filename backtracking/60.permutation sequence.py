import math
class Solution():
    """
    This is permutation sequence by my own implementation by recursively getting all permutations
    Time complexity: O(n!)
    Space complexity: O(n!)
    """
    def getPermutation(self, n, k):
        results = []
        cur = []
        used = [False for i in range(n)]
        self.dfs(results, used, cur, n, k)
        tmp = results[k-1]
        res = ""
        for i in range(n):
            res += str(tmp[i])
        return res

    # this is helper function to get the permutation
    def dfs(self, results, used, cur, n, k):
        if len(cur) == n:
            results.append(cur[:]) # add permutation result into the list
            return

        if len(results) == k:
            return

        for i in range(n):
            if not used[i]:  # if we have not track this in permutation
                used[i] = True
                cur.append(i+1)
                self.dfs(results, used, cur, n, k)
                cur.pop() # pop this up for same level other options
                used[i] = False

    def getPermutation2(self, n, k):
#math.factorial(n)
        
print(Solution().getPermutation(8,39532))
