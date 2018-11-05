def romanToInt(self, s):
    """
    :type s: str
    :rtype: int
    """
    dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000} # dictionary for roman integers

    if not s:
        return
    if len(s) == 1:
        return dict[s]
    res = dict[s[0]] # the first elements
    for r in range(1, len(s)):
        if dict[s[r]] > dict[s[r-1]]:
            res += dict[s[r]] - 2 * dict[s[r-1]]
        else:
            res += dict[s[r]]

    return res
