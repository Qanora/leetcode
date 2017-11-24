class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1,-1]
        n = len(nums)
        left = 0
        right = n - 1
        rLeft = -1
        rRight = -1
        while(True):
            mid = int((left+right)/2)
            print("left" + str(left))
            print("right" + str(right))
            print("mid" + str(mid))
            if nums[n - 1] < target or nums[0] > target:
                break
            if target > nums[mid]:
                left = mid + 1
            if target < nums[mid]:
                right = mid - 1
            if target == nums[mid] or target == nums[left] or target == nums[right] :
                for i in range(left,right + 1,1):
                    if nums[i] == target:
                        rLeft = i
                        break
                for i in range(right,left - 1,-1):
                    if nums[i] == target:
                        rRight = i
                        break
                break
            if left >= right :
                break

        if rLeft != -1 and rRight == -1:
            rRight = rLeft
        if rRight != -1 and rLeft == -1:
            rLeft = rRight
        return [rLeft,rRight]
