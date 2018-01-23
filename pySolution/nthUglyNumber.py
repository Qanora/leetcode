class Solution:
    def nthUglyNumber(self, n):
        ans = [1,2,3,5]
        while len(ans) < n:
            