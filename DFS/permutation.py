# This is leetcode implementation for permutation
class Solution():
    def permute(self, num):
        results = []
        cur = []
        used = [False for i in range(len(num))]
        self.dfs(results, used, cur, num)
        return results

    # this is helper function to get the permutation
    def dfs(self, results, used, cur, num):
        if len(cur) == len(num):
            results.append(cur[:]) # add permutation result into the list
            return

        for i in range(len(num)):
            if not used[i]:  # if we have not track this in permutation
                used[i] = True
                cur.append(num[i])
                self.dfs(results, used, cur, num)
                cur.pop() # pop this up for same level other options
                used[i] = False

print(Solution().permute([5,7,8,9,3,2,1]))
