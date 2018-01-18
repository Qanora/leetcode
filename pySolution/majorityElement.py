class Solution:
    def majorityElement(self, nums):
        table = {}
        ans = [nums[0],1]
        for val in nums:
            if val not in table:
                table[val] = 1
            else:
                table[val] = table.get(val) + 1
                if ans[1] < table.get(val):
                    ans[0] = val
                    ans[1] = table.get(val)
                if ans[1] > len(nums)//2:
                    return ans[0]
        return ans[0]

s = Solution().majorityElement([6,5,5])
print(s)