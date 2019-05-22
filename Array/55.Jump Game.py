"""
My first implementation of jumping game
Time complexity:
Space complexity:
"""
class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        res = False
        if not nums or len(nums) == 0:
            return res
        if len(nums) == 1:
            return True
        return self.dfs(0, nums)

    def dfs(self, start, nums):
        if start >= len(nums)-1:
            return True

        if start < len(nums)-1 and nums[start] == 0: # if start element in the range and it is 0
            return False

        for i in range(nums[start], 0, -1):
            return self.dfs(start+i, nums)
    """
    Hint from youtube
    Time complexity: O(n)
    Space complexity: O(1)
    """
    def canJump2(self, nums):
        if not nums or len(nums) == 0:
            return False
        max_pos = 0
        for i in range(len(nums)):
            if i > max_pos:
                return False
            max_pos = max(nums[i]+i, max_pos)
        return True

nums = [2,3,1,1,4]
nums = [3,2,1,0,4]
nums = [2,5,0,0]
#nums = [2, 0, 0]
if __name__ == "__main__":
    print(Solution().canJump2(nums))
