class Solution:
    def maximumGap(self, nums):
        ans = 0
        if len(nums) < 2:
            return 0
        maxItem = max(nums)
        minItem = min(nums)
        ItemCount = len(nums)
        interval = max(1, (maxItem - minItem)/(ItemCount-1))


s = Solution().maximumGap([1,10000000])
print(s)