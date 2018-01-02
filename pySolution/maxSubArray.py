class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current = big = nums[0]
        for i in nums[1:]:
            total = current + i
            if total > i:
                current = total
            else:
                current = i
            big = max(big, current)
        return big