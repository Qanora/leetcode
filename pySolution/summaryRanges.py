class Solution:
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []

        ans = []
        temp = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] - 1 != nums[i - 1]:
                ans.append(temp[:])
                temp.clear()
                temp.append(nums[i])
            else:
                temp.append(nums[i])
        if temp:
            ans.append(temp[:])

        rAns = []
        for val in ans:
            if len(val) == 1:
                rAns.append(str(val[0]))
            else:
                rAns.append(str(val[0]) + "->" + str(val[-1]))
        return rAns

s = Solution().summaryRanges([0,2,3,4,6,8,9])
print(s)