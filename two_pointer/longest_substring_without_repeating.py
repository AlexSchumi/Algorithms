class Solution(object):
    def lengthOfLongestSubstring(self, s): # This version is naive version of this problem. I will revise to speed up using two pointer
        """     This is brutal solution, which will exceed time limit cuz I do a lot of repeating excution
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        if len(s) == 1:
            return 1
        memory = ''
        max_len = 0 # did not record location
        for i in range(len(s)):
            memory += s[i]
            for j in range(i+1,len(s)):
                if s[j] in memory:
                    break
                else:
                    memory += s[j]
            max_len = max(max_len, len(memory))
            memory = ''
        return max_len


    def lengthOfLongestSubstring_2(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        res = {}
        max_len = 0
        j = 0 # this is left pointer to locate the start position
        for i in range(len(s)):
            if s[i] in res:
                j = max(j, res[s[i]] + 1)

            res[s[i]] = i # store the key and value in dictionary
                             # useful for memorying the location
            max_len = max(max_len, i-j+1)
        return max_len


    def lengthOfLongestSubstring3(self, s):
        if not s:
            return 0
        max_len = -1 #initialize max_len
        res = dict() # dictionary to store
        i = 0
        for j in range(len(s)): # the faster pointer to move around the string
            if s[j] in res:
                i = max(i, res[s[j]] + 1)   # ????????

            res[s[j]] = j
            max_len = max(max_len, j-i+1) #update the maximum length in this situation
        return max_len


print(Solution().lengthOfLongestSubstring("bbtablud"))
print(Solution().lengthOfLongestSubstring("abcabcbb"))
print(Solution().lengthOfLongestSubstring3("bbtablud"))
print(Solution().lengthOfLongestSubstring3("abcabcbb"))
