class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if not num1 or not num2:
            return ""
        if num1 == 0 or num2 == 0:
            return "0"

        if len(num1) > len(num2):
            return self.multiply(num2, num1)

        res = 0
        pos = 1
        cnt = 1
        for j in range(len(num1)-1, -1, -1):
            res += int(num2) * int(num1[j]) * pos
            pos = pos * 10

        return str(res)

print(Solution().multiply(num1 = "123", num2 = "456"))
