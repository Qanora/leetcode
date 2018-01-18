
class Solution(object):
    def largestNumber(self, nums):
        r = ''.join(sorted(map(str, nums), lambda x, y: [1, -1][x + y > y + x]))
        return r.lstrip('0') or '0'

s = Solution().largestNumber([121,12])
print(s)