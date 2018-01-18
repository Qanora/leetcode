class Solution:
    def titleToNumber(self, s):
        count = 1
        ans = 0
        for i in s[::-1]:
            ans += (ord(i) - ord('A') + 1) * count
            count *= 26
        return ans
s = Solution().titleToNumber("AZ")
print(s)
