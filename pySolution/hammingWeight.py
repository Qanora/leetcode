import math


class Solution:
    def hammingWeight(self, n):
        ans = [1431655765, 858993459, 252645135, 16711935, 65535]
        temp = n
        count = 0
        for i in (1, 2, 4, 8, 16):
            b0 = temp & ans[count]
            b1 = temp >> i & ans[count]
            temp = b0 + b1
            count += 1
        return temp


s = Solution().hammingWeight(15)
print(s)