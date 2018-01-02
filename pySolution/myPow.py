class Solution:
    def myPow(self, x, n):
        ans = x
        for _ in range(n-1):
            ans *= x
        ans = "%.5f" % round(ans,5)
        return ans

s = Solution().myPow(2.1,3)
print(s)
print(5%2)