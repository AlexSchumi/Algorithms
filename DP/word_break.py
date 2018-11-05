def wordBreak(s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: bool
    """
    dp = [False] * (len(s) + 1)
    dp[0] = True
    new_s = ' ' + s

    for i in range(1,len(new_s)+1):
        for j in range(i):
            if dp[j] == True and new_s[j+1:i] in wordDict:
                dp[i-1] = True
    return dp[-1]

s = "leetcode" ; wordDict = ["leet", "code"]
#s = "applepenapple"; wordDict = ["apple", "pen"]
#s = "catsandog"; wordDict = ["cats", "dog", "sand", "and", "cat"]
print(wordBreak(s, wordDict))
