# twosum for sorted array, use two-pointer
def twoSum(self, nums, target):
    i = 0
    j = len(nums)-1
    while i < j:
        if nums[i] + nums[j] == target:
            return [i+1,j+1]
        elif nums[i] + nums[j] > target:
            j -= 1
        else:
            i += 1
