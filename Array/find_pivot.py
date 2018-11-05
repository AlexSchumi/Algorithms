class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 0:
            return -1
        if sum(nums[1:]) == 0:
            return 0

        total_sum = sum(nums)
        l, r = 0, total_sum

        for idx in range(1, len(nums)-1):
            l += nums[idx-1]
            r = total_sum - l - nums[idx]
            if l == r:
                return idx

        if total_sum - nums[len(nums)-1] == 0:
            return len(nums) - 1
        return -1

print(Solution().pivotIndex([1, 2, 3]))
