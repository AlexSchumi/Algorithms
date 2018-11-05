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
                    min_len = min(min_len, end - start + 1)
                    min_str = s[start:end+1]

        return min_str



def minWindow2(s, t):
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


S = "ADOBECODEBANC"
T = "ABC"
#S = 'aaaaa'
#T = 'aa'
print(minWindow2(S, T))
