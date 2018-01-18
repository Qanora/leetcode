class Solution:
    def containsNearbyDuplicate(self, nums, k):
        ans = {}
        for i in range(len(nums)):
            if nums[i] not in ans:
                ans[nums[i]] = i
            else:
                if i - ans.get(nums[i]) >= k:
                    return True
        return False

    def containsNearbyDuplicate(self, nums, k):
        dic = {}
        for i, v in enumerate(nums):
            if v in dic and i - dic[v] <= k:
                return True
            dic[v] = i
        return False

s = Solution().containsNearbyDuplicate([-1,-1],1)
print(s)