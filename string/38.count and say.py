class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        """
        This is my implementation of count and say
        """
        if n == 1:
            return "1"

        nth = self.countAndSay(n-1) #nth sequence
        # decode it into n+1 sequence
        res = ""
        tmp = nth[0]
        cnt = 0
        for cur in nth:
            if cur == tmp:
                cnt += 1
            else:
                res += str(cnt)
                res += tmp
                tmp = cur
                cnt = 1
        if cnt != 0:
            res += str(cnt)
            res += tmp
        return res
    """
    This is my implementation without Recursion
    Time complexity: not sure
    Space complexity: O(n)
    """
    def countAndSay2(self, n):
        res = "1"
        i = 1
        while i < n:
            tmp = res[0]
            cnt = 0
            ress = ""
            for cur in res:
                if cur == tmp:
                    cnt += 1
                else:
                    ress += str(cnt)
                    ress += tmp
                    tmp = cur
                    cnt = 1
            if cnt != 0:
                ress += str(cnt)
                ress += tmp
            i += 1
            res = ress
        return res
print(Solution().countAndSay(10)==Solution().countAndSay2(10))
