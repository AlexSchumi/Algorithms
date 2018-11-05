# The first two solution is just using counter in python to solve this problem;
import collections
class Solution:
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        res = False
        if len(s1) > len(s2):
            return res

        l = list(s1)
        length = len(l)

        for i in range(len(s2)-len(s1)+1):
            if s2[i] in s1: # start point
                tmp = list(s2[i:i+length])
                print(tmp)
                #if sorted(l) == sorted(s2[i:i+len(s1)]):
                if len(l) == len(set(l)):
                    if set(l) == set(s2[i:i+len(s1)]):
                        return True
                # check if tmp is permutation of s1
                #if collections.Counter(list(tmp)) == collections.Counter(l):
                #if all(tmp.count(char) == l.count(char) for char in l):
                else:
                    if collections.Counter(list(tmp)) == collections.Counter(l):
                        return True

        return res

    def checkInclusion2(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        res = False
        if len(s1) > len(s2):
            return res

        ctr1 = collections.Counter(s1)
        while i < len(s2) - len(s1) + 1:
            if s2[i] in s1:
                ctr2 = collections.Counter(s2[i: i+len(s1)])
            if ctr1 == ctr2:
                return True
            i += 1
        return res

# This is a method using slide window;
# Since we will have duplicate in s1, we have to store the character counts for slide window;
# think about a way to store window results!!!!!!!!!!!!!!
    def checkInclusion3(self, s1, s2):
        res = False
        if len(s1) > len(s2):
            return res
        a = [ord(x) - ord('a') for x in s1] # string into integer
        b = [ord(x) - ord('a') for x in s2] # string into interger
        target = [0] * 26
        # This is our target window
        for x in a:
            target[x] += 1
        window = [0] * 26 # this is our target window
        for i in range(len(b)):
            window[b[i]] += 1
            if i >= len(a): # if we have slided over s1
                window[b[i-len(a)]] -= 1
            if window == target:
                return True
        return res

print(Solution().checkInclusion3("ab", "eidbaooo"))
