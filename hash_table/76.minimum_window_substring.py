import sys
class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t: #if we do not have any of those two strings
            return ""
        if len(t) > len(s):
            return ""

        res = {}
        min_len = -1
        min_str = ""

        for i in range(len(s)):
            if s[i] in t:
                res[s[i]] = i # store the position of string
                if all(a in res.keys() for a in t): # if all elements have been stored in the hashmap
                # get the length and string
                    start = min(res.values())
                    end = max(res.values())
                    if min_len < 0:
                        min_len = end - start + 1
                        min_str = s[start:end+1]
                    else:
                        if min_len > end - start + 1:
                            min_len = min(min_len, end - start + 1)
                            min_str = s[start:end+1]
        return min_str


    def minWindow2(self, s, t):
        """
        This is second implementation of minimum minWindow
        """
        if len(t) > len(s) or len(t) == 0:
            return ""

        match_cnt = len(t) # this is recording matching count
        # a dict to record how many char we need to match
        word = dict()
        for str in t:
            if str in word:
                word[str] += 1
            else:
                word[str] = 1

        minlen = sys.maxsize
        slow = 0
        res = ""

        for i in range(len(s)):
            if s[i] in word:
                word[s[i]] -= 1
                if word[s[i]] >= 0:
                    match_cnt -= 1

            while match_cnt == 0: #if we have found one example of substring, move the slower pointer
                if (i-slow+1) < minlen:
                    minlen = (i - slow + 1)
                    res = s[slow:i+1] # output
                    #print(res)
                if s[slow] in word:
                    word[s[slow]] += 1
                    if word[s[slow]] > 0:
                        match_cnt += 1
                slow += 1
        return res

S = "ADOBECODEBANC"
T = "ABC"
#S = 'aaaaa'
#T = 'aa'
print(Solution().minWindow2(S, T))
