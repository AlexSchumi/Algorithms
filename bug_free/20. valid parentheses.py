class Solution():
    def isValid(self, s):
        if not s or len(s) == 0:
            return True

        dict = {'(':')', '[':']','{':'}'}
        stack = []
        for t in s:
            if t in dict:
                stack.append(dict[t]) # append parenthese
            else:
                if len(stack) == 0 or stack.pop() != t:
                    return False
        return len(stack) == 0

if __name__ == '__main__':
    print(Solution().isValid("()"))
    print(Solution().isValid("()[]{}"))
    print(Solution().isValid("(]"))
    print(Solution().isValid("([)]"))
    print(Solution().isValid("{[]}"))
    print(Solution().isValid("["))
