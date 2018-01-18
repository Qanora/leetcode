class Solution:
    def findPeakElement(self, nums):
        if not nums:
            return None
        nums.insert(0,nums[0]-1)
        nums.append(nums[-1]-1)
        for i in range(1,len(nums)-1):
            if nums[i-1] < nums[i] > nums[i+1]:
                return i-1

Solution().findPeakElement([1,2,3])