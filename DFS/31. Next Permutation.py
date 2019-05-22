class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        """
        This is my first implementation of nextpermutation by swaping numbers in nums!!! Incorrect
        Time complexity:
        Space complexity:
        """
        if not nums or len(nums) == 0 or len(nums) == 1:
            return nums

        for i in range(len(nums)-1, 0 ,-1):
            if nums[i] - nums[i-1] > 0:
                nums[i], nums[i-1] = nums[i-1], nums[i]
                return nums

        return nums.reverse()

    def nextPermutation2(self, nums):
        """
        Correct thought to solve this problem
        """
        if not nums or len(nums) == 0 or len(nums) == 1:
            return

        smaller = -1
        for i in range(len(nums)-1, 0, -1):
            if nums[i] > nums[i-1]:
                smaller = i - 1
                break

        if smaller == -1:
            nums.reverse()

        larger = -1
        for i in range(len(nums)-1, smaller, -1):
            if nums[i] > nums[smaller]:
                larger = i
                break
        nums[smaller], nums[larger] = nums[larger], nums[smaller]
        nums[smaller+1:] = reversed(nums[smaller+1:])
        return nums

print(Solution().nextPermutation2([1,2,5,4,7,7,6,3]))
