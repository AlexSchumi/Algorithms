class Solution(object):
    """
    This is my implementation of combination sum
    Time complexity: O(2^n)
    Space complexity: O(n)
    """
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ress = []
        res = []
        if not candidates and len(candidates) == 0:
            return ress
        #candidates.sort() # sort for unique
        self.helper2(res, ress, target, 0, candidates)
        return ress

    def helper(self, res, ress, target, i, candidates):
        if sum(res) == target:
            ress.append(res[:]) # use deep copy to avoid bug!!!!!!
            return

        if sum(res) > target:
            return

        if sum(res) < target:
            if res:
                for num in range(i, len(candidates)):
                    res.append(candidates[num])
                    self.helper(res, ress, target, num, candidates)
                    res.pop()
            else:
                for num in range(len(candidates)):
                    res.append(candidates[num])
                    self.helper(res, ress, target, num, candidates)
                    res.pop()

    def helper2(self, res, ress, target, i, candidates):
        if sum(res) == target:
            ress.append(res[:]) # use deep copy to avoid bug!!!!!!
            return

        if sum(res) > target:
            return

        if sum(res) < target:
            for num in range(i, len(candidates)):
                res.append(candidates[num])
                self.helper(res, ress, target, num, candidates)
                res.pop()

print(Solution().combinationSum([2,3,6,7], 7))
print(Solution().combinationSum([2,3,5], 8))
