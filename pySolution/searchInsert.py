class Solution:

    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        mid = -1
        left = 0
        right = n -1

        while(True):
            mid = int((left+right)/2)
            if nums[mid] > target:
                right = mid - 1
            if nums[mid] < target:
                left = mid + 1
            if nums[mid] == target:
                return mid
            print(left,right)
            if left > right:
                break
            print(left,right)
        return  max(left,right)
