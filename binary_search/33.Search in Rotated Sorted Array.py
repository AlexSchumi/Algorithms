"""
This is my implementation of search in rotated sorted array
Time complexity: O(logn)
Space complexity: O(1)

          /   |
         /    |
        /     |
--------------|--------- rotated sorted array
                  /
                 /
                /    
"""
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums or len(nums) == 0:
            return -1
        lo = 0
        hi  = len(nums) - 1

        while (lo + 1 < hi):
            mid = (lo + hi) // 2
            if nums[mid] > nums[hi]:
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target and nums[lo] <= target:
                    hi = mid
                else:
                    lo = mid
            else:
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target and target <= nums[hi]:
                    lo = mid
                else:
                    hi = mid

        if nums[lo] == target:
            return lo
        if nums[hi] == target:
            return hi
        return -1

print(Solution().search([4,5,6,7,0,1,2], target = 3))
