class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums or len(nums) == 0:
            return

        res = [None] * len(nums)
        res[0] = 1
        res_inv = [None] * len(nums)
        res_inv[-1] = 1

        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]

        for j in range(len(nums)-2,-1,-1):
            res_inv[j] = res_inv[j+1]*nums[j+1]

        ab = [res[i]*res_inv[i] for i in range(len(res))]
        return ab

print(Solution().productExceptSelf([1,2,3,4]))
