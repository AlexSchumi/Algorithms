class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        """
        This is my implementation of strStr() by looking at the string directly
        Time complexity: O(nm)
        Space complexity: O(1)
        """
        if not needle or len(needle) == 0:
            return 0
        if len(haystack) < len(needle):
            return -1
        m = len(needle)
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:(i+m)] == needle:
                return i
        return -1

    """
    This is my second implementation of strStr() by using two pointer
    """
    def strStr2(self, haystack, needle):
        return

print(Solution().strStr("aaaaaa", "bba"))
