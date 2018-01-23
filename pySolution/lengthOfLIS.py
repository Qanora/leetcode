class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        n = len(nums)
        dp = [1]*n
        for i in range(len(nums)):
            temp = 0
            for j in range(i-1, -1, -1):
                if nums[j] < nums[i]:
                    temp = max(temp, dp[j])
            dp[i] += temp
        return max(dp)

s = Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])
print(s)