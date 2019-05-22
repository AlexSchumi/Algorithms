# twosum for sorted array, use two-pointer
class Solution:
    """
    My first implementation using hashmap
    """
    def twoSum(self, nums, target):
        array = dict()
        for i in range(len(nums)):
            array[nums[i]] = i # record last apperance index

        for i in range(len(nums)):
            if (target - nums[i]) in nums:
                j = array[target-nums[i]]
                if i != j:
                    return [i,j]

        return [-1,-1]


if __name__ == "__main__":
    print(Solution().twoSum([0,4,3,0],0))
