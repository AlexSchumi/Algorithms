# This is leetcode implementation for combination
class Solution():
    def combine(self, n, k):
        results = []
        cur = []
        # used = [False for i in range(n)]
        self.bfs(results, cur, n, k)
        return results

    # this is helper function to get the permutation
    def bfs(self, results, cur, n, k):
        if len(cur) == k:
            results.append(cur[:]) # add combination results into results
            return

        if cur:
            for i in range(cur[-1], n):
                cur.append(i+1)
                self.bfs(results, cur, n, k) # pass cur to next level
                cur.pop()

        if not cur:
            for i in range(n):
                cur.append(i+1)
                self.bfs(results, cur, n, k)
                cur.pop()

print(Solution().combine(5,2))
print(Solution().combine(10,2))
print(Solution().combine(7,3))
