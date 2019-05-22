class Solution(object):
    """
    This is my first version of this problem
    Time complexity: O(n)
    Space complexity: O(1)
    """
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) == 0:
            return nums

        count = [0] * 3
        for num in nums:
            if num == 0:
                count[0] += 1
            elif num == 1:
                count[1] += 1
            else:
                count[2] += 1

        for i in range(len(nums)):
            if i < count[0]:
                nums[i] = 0
            elif count[0] <= i < count[0] + count[1]:
                nums[i] = 1
            else:
                nums[i] = 2
        return nums
    """
    Follow up to improve this algorithm by onepass algorithm
    """
    def sortColors2(self, nums):
        if not nums or len(nums) == 0:
            return nums
        i = j = 0

        for k in range(len(nums)):
            v = nums[k]
            nums[k] = 2 # change it to the maximum
            if v < 2:
                nums[j] = 1
                j += 1
            if v == 0:
                nums[i] = 0
                i += 1
        return nums

nums = [2,0,2,1,1,0]
if __name__ == "__main__":
    print(Solution().sortColors2(nums))
