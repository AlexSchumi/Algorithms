import sys
class Solution(object):
    """
    This is my implementation of 3sum closet using two pointer, loop over i, use j, k two pointers;
    j is designed to move right and k is designed to more left.

    Time complexity: O(nlogn + n^2)
    Space complexity: O(1)
    """
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if not nums or len(nums) <= 2:
            return None
        nums.sort() # sort s
        diff = sys.maxsize
        for i in range(len(nums)-2):
            if i >= 1 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while (j < k):
                s = nums[i] + nums[j] + nums[k]
                if abs(s - target) < diff:
                    diff = abs(s - target)
                    res = s
                if s > target:
                    k -= 1 # if sum is larger, k move to the left
                    while k > 0 and k < len(nums)-1 and nums[k] == nums[k+1]: # k is designed to move left
                        k -= 1
                elif s < target:
                    j += 1 # if sum is smaller, j move to the right
                    while j < len(nums)-1 and j > 0 and nums[j] == nums[j-1]: # j is designed to move right
                        j += 1
                else:
                    return target # sum is equal to the target, return target
        return res
    """
    This is my second implementation of 3sum closet using brutal force (TLE)
    """
    def threeSumClosest2(self, nums, target):
        if not nums or len(nums) <= 2:
            return None
        diff = sys.maxsize
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    s = nums[i] + nums[j] + nums[k]
                    if abs(s-target) < diff:
                        diff = abs(s-target)
                        res = s
        return res
print(Solution().threeSumClosest2([1,1,-1,-1,3],-1))
