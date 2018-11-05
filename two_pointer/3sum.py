import collections
from collections import Counter
## We can utilize the sort and use two pointer to solve this questions.
## 去重！！！！！！！！！！！！！！！！
class Solution(object):
    def threesum(self, nums): ## This method is my try for this problem
        """
        :type nums: List[int]
        :rtype List[List[int]]
        """
        if len(nums) <= 2: # edge case when we only have 2 elements in nums
            return None

        i = 0
        j = 1

        #nodup_nums = list(set(nums))
        nodup_nums = nums
        memory = []
        print(nodup_nums)
        l = []

        for i in range(len(nodup_nums)-2):
            for j in range(i+1,len(nodup_nums)-1):
                if -(nodup_nums[i] + nodup_nums[j]) in nodup_nums[j+1:] and Counter([nodup_nums[i],nodup_nums[j],-(nodup_nums[i]+nodup_nums[j])]) not in memory: # and it is not already in the l
                    l.append([nodup_nums[i],nodup_nums[j],-(nodup_nums[i]+nodup_nums[j])])
                    memory.append(Counter([nodup_nums[i],nodup_nums[j],-(nodup_nums[i]+nodup_nums[j])]))

        return l


    def threesum_sort(self, nums):
        nums.sort() # sort nums， 利用sort去解决问题
        results = []
        for i in range(len(nums)-2):
            l, r = i + 1, len(nums) - 1
            if i > 0 and nums[i] == nums[i-1]:
                continue # break out of this loop and continue on next loop # pass do not do anything in this loop # break jump out of loop
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s > 0:
                    r -= 1
                elif s < 0:
                    l += 1
                else:
                    results.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1; r -= 1
        return results

print(Solution().threesum_sort([1,2,-2,-1,-1,0]))
