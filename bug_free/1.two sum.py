class Solution():
    def two_sum(self, nums, target):
        if not nums or len(nums) == 0:
            return []
        hashmap = dict()
        for i in range(len(nums)):
            hashmap[nums[i]] = i # record index

        for i in range(len(nums)):
            if target - nums[i] in hashmap and hashmap[target - nums[i]] != i:
                return [i, hashmap[target - nums[i]]]
        return []

    def twoSum(self, nums, target):
        if not nums or len(nums) < 2:
            return [-1, -1]
        hashmap = dict()

        for i in range(len(nums)):
            if target - nums[i] in hashmap:
                return [i, hashmap[target-nums[i]]]
            hashmap[nums[i]] = i

if __name__ == '__main__':
    print(Solution().twoSum([2, 7, 11, 15], target = 9))
