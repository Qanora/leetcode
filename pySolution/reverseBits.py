class Solution:
    def reverseBits(self, n):
        res = 0
        for i in range(32):
            res = res << 1 | (n >> i & 1)
        return res
s = Solution().reverseBits(43261596)
print(s)