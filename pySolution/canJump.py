class Solution:
    def canJump(self, nums):
        if len(nums) == 1:
            return True
        ans = []
        for index in range(len(nums)):
            if ans and nums[index] == 0 and max(ans) <= index+ nums[index] and index != len(nums) -1:
                return False
            ans.append(index+nums[index])
        print(ans)
        if ans[0] == 0:
            return False
        return True

s = Solution().canJump([2,0,0])
print(s)
