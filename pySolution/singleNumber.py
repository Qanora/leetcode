class Solution:
    def singleNumber(self, nums):
        A, B = 0, 0
        for val in nums:
            PA = A
            A = (B & val) | (A & (~val))
            B = ((~PA) & (~B) & val) | (B & (~val))
        return B

s = Solution().singleSolution([1])
print(s)