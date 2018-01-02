import sys


class Solution:
    def merge(self, nums1, m, nums2, n):
        cur_m = m
        while len(nums1) > m:
            nums1.pop(cur_m)
        nums1.insert(0,-sys.maxsize)
        nums1.insert(m+1,sys.maxsize)
        cur_m = 0
        while nums2:
            if nums1[cur_m] <= nums2[0] and nums1[cur_m+1] >= nums2[0]:
                nums1.insert(cur_m+1, nums2.pop(0))
                cur_m += 1
            else:
                cur_m += 1
        nums1.pop(0)
        nums1.pop()

nums1 = [1,2,3,4,5]
nums2 = [6,7,8,9]
Solution().merge(nums1,5,nums2,4)
print(nums1)