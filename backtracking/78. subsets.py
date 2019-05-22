class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ress = []
        #res = []
        #used = [0] * len(nums)
        #ress.append(res[:])
        #if not nums or len(nums) == 0:
        #    return ress
        nums.sort()
        #self.dfs(nums.sort(), used, res, ress, 0)
        self.dfs2(nums, [], ress, 0)
        return ress

    def dfs(self, nums, used, res, ress, i):
        if len(res) == len(nums): # if we have reached the total number of subsets
            return

        if not res or len(res) == 0:
            for i in range(len(nums)):
                used[i] = 1
                res.append(nums[i])
                ress.append(res[:])
                self.dfs(nums, used, res, ress, i)
                used[i] = 0
                res.pop()
        else:
            for i in range(i, len(nums)):
                if used[i] == 0:
                    used[i] = 1
                    res.append(nums[i])
                    ress.append(res[:]) # deep copying!!!!!! in recursion
                    self.dfs(nums, used, res, ress, i)
                    used[i] = 0
                    res.pop()

    def dfs2(self, nums, res, ress, i):
        ress.append(res)
        for i in range(i, len(nums)):
            self.dfs2(nums, res+[nums[i]], ress, i+1)

    # Iteratively in leetcode discussion
    def subsets2(self, nums):
        res = [[]]
        for num in sorted(nums):
            res += [item+[num] for item in res]
        return res


if __name__ == "__main__":
    nums = [1,2,3]
    print(Solution().subsets2(nums))
