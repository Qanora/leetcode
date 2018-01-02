class Solution:
    def search(self, nums, target):
        if not nums:
            return False
        l, r = 0, len(nums)-1
        while l <= r:
            mid = l + (r - l)//2
            if target == nums[mid] or target == nums[l] or target == nums[r]:
                return True
            if nums[mid] < nums[l] and nums[mid] < nums[r]:
                if target > nums[mid] and target < nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            elif nums[mid] > nums[l] and nums[mid] > nums[r]:
                if target > nums[l] and target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                l += 1
        return False

s = Solution()
for i in range(1,11):
    w = s.search([1],1)
    print(i,w)

"""
[9,10,1,2,3,4,5,6,7,8]
9         3         8
[3,4,5,6,7,8,9,10,1,2]
3         8         2
"""