class Solution:
    def sortColors(self, nums):
        colorCount = [0,0,0]
        for val in nums:
            colorCount[val] += 1
        nums.clear()
        for index in range(len(colorCount)):
            for _ in range(colorCount[index]):
                nums.append(index)

p = [0,1,2,0,1,2,0,1,2]
Solution().sortColors(p)
print(p)