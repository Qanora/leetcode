class Solution:
    def findKthLargest(self, nums, k):
        for i in range(k-1):
            nums.remove(max(nums))
        print(nums)
        return max(nums)

s = Solution().findKthLargest([3,2,1,5,6,4],2)
print(s)