class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        for i in range(l+1):
            if i not in nums:
                return i

    def missingNumber2(self, nums):
        l = len(nums)
        return l*(l+1) // 2 - sum(nums)


if __name__ =='__main__':
    print(Solution().missingNumber2([3,1,0]))
