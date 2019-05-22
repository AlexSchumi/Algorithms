class Solution(object):
    """
    This is my implementation of valid parentheses using stack, first in last out principle
    Time complexity: O(n)
    Space complexity: O(1)   Nov.7
    """
    
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #left = ['(', '[', '{']
        #right = [')', '}', ']']
        dict = {'(':')', '[':']', '{':'}'} # dictionary to traverse for parentheses
        stack = []
        if not s:
            return True
        #if s[0] in dict.values():
        #    return False
        for str in s:
            if str in dict:
                stack.append(dict[str]) # append the right parenthese in stack
            else:
                # if we have nothing to pop up to compare
                if len(stack) == 0: # stack = [], stack is not None and len(stack) == 0
                    return False
                else:
                    cur = stack.pop()
                    if cur != str:
                        return False
        return len(stack) == 0

print(Solution().isValid("()"))
print(Solution().isValid("()[]{}"))
print(Solution().isValid("([)]"))
print(Solution().isValid("{[]}"))
print(Solution().isValid("[]["))
