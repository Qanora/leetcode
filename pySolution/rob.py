class Solution:
    def rob(self, nums):
        if len(nums) < 3:
            return 0
        def robSingle(nums):
            last = 0
            now = 0
            for i in nums:
                last,now = now,max(now,last+i)
            return now
        return max(robSingle(nums[:-1]), robSingle(nums[1:]))

s = Solution().rob([1])
print(s)
