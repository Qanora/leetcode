import copy
class Solution:
    def removeDuplicates(self, nums):
        count = True
        target = len(nums)
        ans = [nums[0]] if nums else []
        for i in range(1,len(nums)):
            last = nums[i-1]
            if last == nums[i] and count:
                count = False
                ans += [nums[i]]
            elif last != nums[i]:
                ans += [nums[i]]
                count = True
        now = len(ans)
        while now < target:
            ans += [0]
            now += 1
        nums.clear()
        nums = copy.deepcopy(ans)
        print(nums)
        print(len(nums))
        return len(nums)

Solution().removeDuplicates([1,1,1,2,2,2,3,3,3])
