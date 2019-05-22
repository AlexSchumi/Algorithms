"""
Think deeply in this example,
why we use binary search and how it works;
"""

class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 1:
            return 1
        lo, hi = 1, x
        while lo + 1 < hi:
            mid = (lo + hi) // 2
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                #hi = mid - 1
                hi = mid
            else:
                lo = mid
                #lo = mid + 1
        #return min(lo, hi)
        return lo

print(Solution().mySqrt(18))
