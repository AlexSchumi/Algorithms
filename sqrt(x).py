def mySqrt(x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        if x == 1:
            return 1

        mid = x // 2

        while mid * mid >= x:
            if mid * mid == x:
                return mid
            else:
                mid = mid // 2
        return mid

print(mySqrt(9))
