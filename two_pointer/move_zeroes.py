class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return None

        i = 0
        j = 1

        while j <= len(nums)-1:
            if nums[i] == 0:
                if nums[j] != 0:
                    nums[i], nums[j] = nums[j], nums[i] # swap two values
                    i += 1
                    j += 1 # move pointer
                else:
                    j += 1
            else:
                i += 1
                j += 1

    def moveZeroes2(self, nums):
        if not nums:
            return nums
        j = 0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[i], nums[j] = nums[j], nums[i] # swap two elements
                j += 1

        return nums



nums = [1,0,3,12,0]
Solution().moveZeroes2(nums)
print(nums)
