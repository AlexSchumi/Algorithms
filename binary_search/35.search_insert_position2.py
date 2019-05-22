class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target < nums[0] or not nums:
            return 0
        if target > nums[-1]: # if target is greater than the last element of nums
            return len(nums)

        s = 0
        e = len(nums) - 1
        while (s <= e):
            m = (s + e) // 2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                e = m - 1
                #e = m
            else:
                s = m + 1
                #s = m
        if nums[s] < target:
            return s + 1
        else:
            return s

print(Solution().searchInsert([1,3,5,6],5))
print(Solution().searchInsert([1,3,5,6],2))
print(Solution().searchInsert([1,3,5,6],7))
print(Solution().searchInsert([1,3, 5, 6],0))
