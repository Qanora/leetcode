class Solution:
    def twoSum(self, numbers, target):
        l, r = 0, len(numbers)-1
        sum = numbers[l] + numbers[r]
        while sum != target:
            if sum < target:
                l += 1
            else:
                r -= 1
            sum = numbers[l] + numbers[r]
        return [l+1, r+1]

s = Solution().twoSum([2,7,11,15],9)
print(s)