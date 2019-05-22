class Solution():
    def longestCommonPrefix(self, strs):
        if not strs or len(strs) == 0:
            return ""
        min_len = min(list(map(len, strs)))
        res = 0
        for i in range(min_len):
            w = strs[0][i] # must satisfy
            for j in range(len(strs)):
                if strs[j][i] != w:
                    return strs[0][:res]
            res += 1
        return strs[0][:res]

    def getcommon(str1, str2):
        l = min(len(str1),len(str2))
        res = 0
        for i in range(l):
            if str1[i] != str2[i]:
                break
            else:
                res += 1
        return res

if __name__ == '__main__':
    print(Solution().longestCommonPrefix(["flower","flow","flight"]))
