class Solution(object):  # This is my implementation, kind of brutal force
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        r = len(s)
        max_len = 0
        max_string = ''
        for l in range(len(s)):
            while s[l:r] != s[l:r][::-1]:
                r -= 1
            if len(s[l:r]) > max_len:
                max_string = s[l:r]
                max_len = len(s[l:r])
            r = len(s) # set r to be the length of the string to start next round iter;

        return max_string

    # The second function is to scan from middle to end
    def longestPalindrome2(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_string = ''
        for l in range(len(s)):
            tmp = self.helper(s, l, l+1)
            if len(tmp) > len(max_string):
                max_string = tmp
            tmp = self.helper(s, l, l)
            if len(tmp) > len(max_string):
                max_string = tmp
        return max_string

    def helper(self, s, l, r):
        while(l >= 0 and r < len(s) and s[l] == s[r]):
            l -= 1
            r += 1

        return s[l+1:r]

    # The third one is to use DP to solve this problem
    # DP is kind of remember last results to update this results

    """
    time complexity: O(n^2)
    space complexity: O(n^2)
    """
    def longestPalindrome3(self, s):
        if not s:
            return s

        max_len = 0
        max_string = ''
        dp = [[None] * len(s) for i in range(len(s))]
        for i in range(len(s)):
            for j in range(0, i + 1):
                dp[j][i] = s[j] == s[i] and ((i - j <= 2) or dp[j+1][i-1])
                if dp[j][i]:
                    if (i - j + 1) > max_len:
                        max_len = i - j + 1
                        max_string = s[j:i+1]
        return max_string

print(Solution().longestPalindrome3("cbbd"))
