class Solution:
    """
    This is my first implementation of generateParenthesis
    Time complexity: ????? time complexity for recursion
    space complexity: O(1)       Nov.7
    """
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = ''
        ress = []
        if n == 0: # edge case when we have n is 0
            return ress
        res += '(' # the first element must be '('
        used = 1  # used is to record how many '(' we have used in the current string
        self.helper(n, used, res, ress)
        return ress

    def helper(self, n, used, res, ress):
        #if len(res) == 2*n: # exit of recursion
        #    ress.append(res)
        #    return
        if used == n and len(res) < 2*n: # if we have used all '(', we have no recursion ahead, add ')' in res and return
            while(len(res) < 2*n):
                res += ')'
            ress.append(res)
            return

        for item in ['(', ')']:
            if item == '(':
                self.helper(n, used + 1, res+'(', ress)
            if item == ')':
                res += ')'
                if len(res) - used <= used:
                    self.helper(n, used, res, ress)
                    res = res[:len(res)-1]

    """
    This is other people's implementation of generateParenthesis
    Time complexity: O(n!)
    Space complexity: O(n)
    it satisfies catlan number, and we can say that the time complexity is factorial of n
    """
    def generateParenthesis2(self, n):
        res = []
        if n == 0:
            return res
        self.helper2(res, "", n, n)
        return res

    def helper2(self, res, s, left, right):
        if left > right:
            return
        if left==0 and right == 0:
            res.append(s)
        if left > 0:
            self.helper2(res, s + '(', left - 1, right)
        if right > 0:
            self.helper2(res, s + ')', left, right - 1)

print(Solution().generateParenthesis2(3))
