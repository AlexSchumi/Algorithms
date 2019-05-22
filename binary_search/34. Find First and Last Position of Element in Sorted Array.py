class Solution:
    """
    This is my first implementation of find first and last of target in nums Nov/15/2018
    Time complexity: O(logn)
    Space complexity: O(1)
    """
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = []
        if not nums or len(nums) == 0:
            return res
        res.append(self.findFirst(nums, target))
        res.append(self.findLast(nums, target))
        return res

    def findFirst(self, nums, target):
        lo = 0
        hi = len(nums) - 1

        while(lo + 1 < hi):
            mid = (hi - lo) // 2 + lo
            if nums[mid] == target:
                hi = mid
            elif nums[mid] > target:
                hi = mid
            else:
                lo = mid
        if nums[lo] == target:
            return lo
        elif nums[hi]== target:
            return hi
        else:
            return -1

    def findLast(self, nums, target):
        lo = 0
        hi = len(nums) - 1
        while(lo + 1 < hi):
            mid = (hi - lo) // 2 + lo
            if nums[mid] == target:
                lo = mid
            elif nums[mid] > target:
                hi = mid
            else:
                lo = mid
        if nums[hi] == target:
            return hi
        elif nums[lo]== target:
            return lo
        else:
            return -1

print(Solution().searchRange([5,7,7,8,8,10], 8))
