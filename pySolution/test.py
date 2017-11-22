class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        pivot = len(nums) - 2
        while pivot >= 0 and nums[pivot] >= nums[pivot + 1]:
            pivot -= 1
        print("pivot = " + str(pivot))
        if pivot >= 0:
            pivot2 = len(nums) - 1
            while pivot2 >= 0 and nums[pivot] >= nums[pivot2]:
                pivot2 -= 1
            print(nums[pivot])
            print(nums[pivot2])
            print("pivot2 = " + str(pivot2))
            nums[pivot], nums[pivot2] = nums[pivot2], nums[pivot]
        nums[pivot + 1:] = nums[pivot + 1:][::-1]

nums = [3,1,2]
Solution().nextPermutation(nums)
print(nums)