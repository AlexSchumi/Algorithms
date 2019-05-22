class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or len(s) == 0:
            return 0
        print(s.split())
        return len(s.split()[-1])

if __name__ == "__main__":
    print(Solution().lengthOfLastWord(" "))
