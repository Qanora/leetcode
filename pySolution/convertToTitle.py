class Solution(object):
    def convertToTitle(self, n):
        res, caps = '', [chr(i + 65) for i in xrange(26)]
        print(caps)
        while n:
            n, rem = divmod(n - 1, 26)
            print(n,rem)
            res = caps[rem] + res
        return res

s = Solution().convertToTitle(52)
print(s)