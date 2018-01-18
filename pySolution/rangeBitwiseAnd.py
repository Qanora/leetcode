class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == n: return m

        cnt = 1
        mask = ~((1 << cnt) - 1)
        print(bin(mask))
        while (m & mask) != (n & mask):
            print(bin(m),bin(n))
            cnt += 1
            mask = ~((1 << cnt) - 1)
            print(bin(mask))
        return m & mask
s = Solution().rangeBitwiseAnd(5,6)
print(s)