class Solution(object):
    """
    This is my implementation of letter combination of phone number
    """
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dict = {'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],\
        '6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
        res = ''
        ress = []
        if not digits:
            return ress

        curr = 0
        self.helper(digits, dict, curr, res, ress)
        return ress

    def helper(self, digits, dict, curr, res, ress):
        if curr >= len(digits): # if we have traverse over all the digits
            ress.append(res)
            return

        for letter in dict[digits[curr]]:
            res += letter # append the letter
            self.helper(digits, dict, curr+1, res, ress)
            if len(res) == 1:
                res = ''
            else:
                res = res[:len(res)-1]

print(Solution().letterCombinations('23456'))
