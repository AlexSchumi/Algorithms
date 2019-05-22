class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        #if nums[0] == nums[len(nums)-1] or len(nums) == 1:
        #    return 1
        j = 0  # the first element of unique value
        cnt = 1
        for i in range(len(nums)):
            if nums[i] == nums[j]: # if this value is equal to nums[j]
                continue
            else:
                cnt += 1
                j += 1
                nums[j], nums[i] = nums[i], nums[j]
                #nums[j] = nums[i]

        #for i in range(cnt-1):
        #    print(nums[i])
        return cnt

myarray = [1,1,1,2,2,3,3,4,5]
print(Solution().removeDuplicates(myarray))
print(myarray[:5])
