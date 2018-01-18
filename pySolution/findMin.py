class Solution:
    def findMin(self, nums):
        if nums[0] < nums[-1]:
            return nums[0]
        l = 0
        r = (len(nums)-1)
        while r > l:
            mid = l + (r-l) // 2
            if mid == l or mid == r:
                break
            if nums[l] <= nums[mid] > nums[r]:
                l = mid + 1
            elif nums[l] > nums[mid] <= nums[r]:
                r = mid - 1
            else:
                r -= 1
        return (l,r)

s = Solution()
ans = [0,1,1,1,2,2,2,3,3]
for i in range(len(ans)):
    print(ans[i:]+ans[:i], s.findMin(ans[i:] + ans[:i]))