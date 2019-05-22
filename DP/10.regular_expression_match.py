class Solution:
    def isMatch(self, s, p):
        """
        '.': mateches any single character
        '*': matches zero or more of the preceding elements
        """
        dp = [False] * len(s)
        special_pos = [None] * len(s) # This is array to record position of special character
        for i in range(len(s)):
            if i >= len(p) and p[i-1] != '*':
                return False
            if s[i] == p[i]:
                dp[i] = True
            if s[i] != p[i]: # the case when s[i] != p[i]
                if p[i] == '.':
                    dp[i] = True
                if p[i] == '*' and p[i-1] == '.':
                    dp[i] = True
                if p[i] == '*' and s[i] == s[i-1]:
                    dp[i] = True
        return all([x == True for x in dp])
    """
    I am gonna try this problem again using dp and dfs
    first, I assume that len(p) <= len(s)
    """

    def isMatch2(self, s, p):
        if len(p) < len(s) and ('*' not in p): # when we do not have * to increase the length of p
            return False
        if not s and p is not None:
            return False

        dp = [0] * len(s)
        dp[0] = 1
        return self.helper(dp, s, p, idx = 1)
        #return sum(dp) == len(s)

    def helper(self, dp, s, p, idx):
        """
        :type dp: List
        :type s: original string
        :type p: regular expression string
        :type cur: current string
        :res: List[string]
        """
        #print(idx)
        if idx == len(s): # if our cur string has the same length of s, return
            #print('Yes')
            return sum(dp) == len(s)
        if s[idx] == p[idx]:
            dp[idx] = 1
        else:
            if p[idx] == '.':
                dp[idx] = 1
                return self.helper(dp, s, p[:idx]+s[idx]+p[idx:], idx+1)
            if p[idx] == '*' and s[idx-1] == s[idx]:
                dp[idx] = 1
                return self.helper(dp, s, p[:idx]+s[idx]+p[idx:], idx+1)
            if p[idx] == '*' and p[idx-1] == '.':
                dp[idx] = 1
                return self.helper(dp, s, p[:idx]+s[idx]+p[idx:], idx+1)
        #self.helper(dp, s, p, idx+1)
        return False

print(Solution().isMatch2(s = "mississippi", p = "mis*is*p*."))
print(Solution().isMatch2(s = "aa", p = "a."))
print(Solution().isMatch2(s = "aab", p = "c*a*b"))
