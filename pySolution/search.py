class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        n = len(nums)
        if nums[0] > nums[n - 1]:
            if target >= nums[0]:
                for i in range(n):
                    if target == nums[i]:
                        return i
                    if nums[i] < nums[i - 1]:
                        break
            else:
                for i in range(n - 1,-1,-1):
                    if target == nums[i]:
                        return i
                    if nums[i] < nums[i - 1]:
                        break
            return -1
        else:
            if target <= nums[0]:
                for i in range(n):
                    if target == nums[i]:
                        return i
                    if nums[i] < nums[i - 1]:
                        break
            else:
                for i in range(n - 1,-1,-1):
                    if target == nums[i]:
                        return i
                    if nums[i] < nums[i - 1]:
                        break
            return -1

Solution().search([4,5,6,7,0,1,2],6)