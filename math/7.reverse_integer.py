class Solution(object):
    def reverse(self, x):
        if not x:
            return

        res = ''
        tmp = str(x)
        if x > 0:
            for i in range(len(tmp)):
                res += tmp[len(tmp)-1-i]

        if x < 0:
            for i in range(len(tmp)-1):
                res += tmp[len(tmp)-1-i]

        for r in range(len(res)):
            if res[r] != '0':
                break

        if x > 0:
            return int(res[r:])
        if x < 0:
            return -1 * int(res[r:])


    def reverse2(self, x):
        if not x or x == 0:
            return x
        if x > 2**31-1 or x < -1*2**31:
            return 0
        tmp = str(x)
        if x > 0:
            res = int(tmp[::-1])
        if x < 0:
            res = -1*int(tmp[::-1][:len(tmp)-1])

        return res

print(Solution().reverse2(-1230))
print(Solution().reverse(-1230))
