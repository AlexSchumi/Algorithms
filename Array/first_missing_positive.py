class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 1

        nums.sort()

        if nums[-1] < 0:
            return 1
        pos = 0

        for i in range(len(nums)):
            if nums[i] <= 0:
                continue # go to the next iteration
            else:
                if nums[i] <= pos:
                    pass
                else:
                    pos += 1
                    if nums[i] == pos:
                        pass
                    else:
                        return pos

        return nums[-1] + 1

nums = [3,-1,23,7,21,12,8,9,18,21,-1,16,1,13,-3,22,23,13,7,14,3,6,4,-3]
nums.sort()
print(nums)
print(Solution().firstMissingPositive([3,-1,23,7,21,12,8,9,18,21,-1,16,1,13,-3,22,23,13,7,14,3,6,4,-3]))
