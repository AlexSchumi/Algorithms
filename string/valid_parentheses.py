class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        d = {'(':')', '[': ']', '{':'}'}

        if not s:
            return True

        memory = []
        for char in s:
            if char in d:
                memory.append(d[char])
            else:
                if memory == [] or memory.pop() != char: # if we have corresponding parenthese without parent
                    return False

        return len(memory) == 0

print(Solution().isValid('()'))
print(Solution().isValid('(('))
print(Solution().isValid('))'))
print(Solution().isValid(']'))
