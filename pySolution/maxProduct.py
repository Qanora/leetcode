class Solution:
    # def maxProduct(self, nums):
    #     count = self.findMaxProduct(nums)
    #     flag = True
    #     for i in range(len(nums)-1):
    #         if nums[i] < 0 and flag:
    #             count = max(count, self.findMaxProduct(nums[i+1:]))
    #             flag = False
    #         if nums[i] == 0:
    #             flag = True
    #     return count
    #
    # def findMaxProduct(self, nums):
    #     count = nums[0]
    #     stack = [nums[0]]
    #     for val in nums[1:]:
    #         if val * stack[-1] > 0:
    #             temp = stack.pop() * val
    #             count = max(count, temp)
    #             stack.append(temp)
    #         elif val * stack[-1] == 0:
    #             stack.append(val)
    #         else:
    #             stack.append(stack.pop() * val)
    #         count = max(count, val)
    #     return count

    def maxProduct(self, nums):
        maximum = big = small = nums[0]
        for n in nums[1:]:
            temp1 = n
            temp2 = n * big
            temp3 = n * small
            big, small = max(n, n * big, n * small), min(n, n * big, n * small)
            maximum = max(maximum, big)
        return maximum

s = Solution().maxProduct([2,-5,-2,-4,3])
print(s)