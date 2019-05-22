class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # 分解指数until 1

        if n > 0:
            return self.pow(x, n)
        elif n < 0:
            return 1/self.pow(x,n)
        else:
            return 1

    def pow(self, x, n):
        if n == 1:
            return x
        if n == 0:
            return 1
        y = self.pow(x, n // 2)

        if n % 2 == 0:
            return y * y
        else:
            return y * y * x

print(Solution().myPow(2.0, 10))
