class Solution:
    def permuteUnique(self, nums):
        ans = [[]]
        for n in nums:
            ans = [l[:i] + [n] + l[i:] for l in ans for i in range((l+[n]).index(n)+1)]
        return ans

s = Solution().permuteUnique([1,2,3])
print(s)
