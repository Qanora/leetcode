class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def jump(self, nums):
        n, start, end, step = len(nums), 0, 0, 0
        while end < n - 1:
            step += 1
            maxend = end + 1
            for i in range(start, end + 1):
                if i + nums[i] >= n - 1:
                    return step
                maxend = max(maxend, i + nums[i])
            start, end = end + 1, maxend
        return step

#[5,9,3,2,1,0,2,3,3,1,0,0]
s = Solution().jump([5,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
print(s)