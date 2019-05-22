class Solution:
    """
    This is my first implementation of add addBinary by force brutal!!!! Too long
    Time complexity:
    Space complexity:
    """
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res = ""
        if not a and not b:
            return ""
        if not a:
            return b
        if not b:
            return a
        la = len(a)
        lb = len(b)
        flag = 0

        for i in range(min(la, lb)):
            if flag == 1:
                if a[la-1-i] == '1' and b[lb-1-i] == '1':
                    res += '1'
                elif a[la-1-i] == '1' or b[lb-1-i] == '1':
                    res += '0'
                else:
                    flag = 0
                    res += '1'
            else:
                if a[la-1-i] == '1' and b[lb-1-i] == '1':
                    res += '0'
                    flag = 1
                elif a[la-1-i] == '1' or b[lb-1-i] == '1':
                    res += '1'
                else:
                    res += '0'
        if la == lb:
            if flag == 1:
                res += '1'
            return res[::-1]
        elif la > lb:
            for j in range(la-lb-1, -1, -1):
                if flag == 1:
                    if a[j] == '1':
                        res += '0'
                    else:
                        res += '1'
                        flag = 0
                else:
                    res += a[j]
                    flag = 0
        else:
            for j in range(lb-la-1, -1, -1):
                if flag == 1:
                    if b[j] == '1':
                        res += '0'
                    else:
                        res += '1'
                        flag = 0
                else:
                    res += b[j]
                    flag = 0
        if flag == 1:
            res += '1'
        return res[::-1]

    """
    This solution is based on recursive solution in leetcode discussion
    Time complexity: 
    """
    def addBinary2(self, a, b):
        if len(a) == 0 and len(b) == 0: return ''
        if len(a) == 0: return b
        if len(b) == 0: return a
        if a[-1] == '1' and b[-1] == '1':
            return self.addBinary2(self.addBinary2(a[:-1], b[:-1]),'1')+'0' # carry 1 in this condition
        elif a[-1] == '0' and b[-1] == '0':
            return self.addBinary2(a[:-1], b[:-1])+'0'
        else:
            return self.addBinary2(a[:-1], b[:-1])+'1'

print(Solution().addBinary2('1010','1011'))
