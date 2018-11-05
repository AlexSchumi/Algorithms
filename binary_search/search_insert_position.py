class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums) - 1

        while (start + 1 < end):
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1

        if start == end:
            if nums[start] == target:
                return start
            elif nums[start] > target:
                return max(start-1, 0)
            else:
                return start + 1
        else:
            if nums[start] > target:
                return max(start-1, 0)
            elif nums[end] < target:
                return end + 1
            else:
                return start + 1

#print(Solution().searchInsert([1,3,5,6],5))
#print(Solution().searchInsert([1,3,5,6],2))
#print(Solution().searchInsert([1,3,5,6],7))
print(Solution().searchInsert([1,3],2))
