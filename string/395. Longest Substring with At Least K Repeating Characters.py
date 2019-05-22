class Solution(object):
    """
    This is my first implementation of this question using brutal force// TLE:(
    Time complexity:
    Space complexity:
    """
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        cnt = 0
        if not s or len(s) < k:
            return cnt
        if k == len(s):
            cnt = max(s.count(s[0]),cnt)

        for i in range(len(s)-k):
            for j in range(len(s), i+k-1, -1):
                l = list(s[i:j])
                #print(j)
                if all([l.count(w) >= k for w in l]):
                    cnt = max(j-i, cnt)
                    break # jump out of this loop since we have found the maximum in this i
        return cnt

    """
    This is second implementation to speed up brutal force algorithm
    """
    def longestSubstring2(self, s, k):
        if not s or len(s) == 0:
            return 0
        if len(s) < k:
            return 0

        start = 0
        end = len(s)
        max_len = 0
        i = 0
        cnt = [0] * 26
        for w in s:
            cnt[ord(w) - ord('a')] += 1 # get cnt vector in this step

        while i < end:

            while i < end and cnt[ord(s[i]) - ord('a')] < k:
                i += 1

            j = i #start from i to search for longer string
            while j < end and cnt[ord(s[j]) - ord('a')] >= k:
                j += 1

            if i == start and j == end:
                return end - start

            tmp_cnt = [0] * 26 # set a tmp_cnt for memorizing
            flag = 0

            for idx in range(end-1, j, -1):
                #print(s[idx])
                tmp_cnt[ord(s[idx]) - ord('a')] += 1
                if cnt[ord(s[idx]) - ord('a')] - tmp_cnt[ord(s[idx]) - ord('a')] < k:
                    flag = 1
                    break

            if flag == 0:
                max_len = max(max_len, j - i)
            i = j
        return max_len

#print(Solution().longestSubstring2("abacbbc",2))
#print(Solution().longestSubstring2(s = "ababbc", k = 2))
print(Solution().longestSubstring2("ababacb", 3))
