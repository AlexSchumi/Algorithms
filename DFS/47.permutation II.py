"""
:type nums: List[int]
:rtype: List[List[int]]
"""
class Solution():
    def permuteUnique(self, num):
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

        dict = [] # memory for used duplicates
        for i in range(len(num)):
            if not used[i]:  # if we have not track this in permutation
                if num[i] in dict:
                    continue # no further recursion
                else:
                    dict.append(num[i])
                used[i] = True
                cur.append(num[i])
                #print(cur)
                self.dfs(results, used, cur, num)
                cur.pop() # pop this up for same level other options
                used[i] = False

print(Solution().permuteUnique([1,1,2,1]))
