class Solution:
    def nextPermutation(self, nums):
        flag = True
        for i in reversed(range(len(nums))):
            if(i - 1 >= 0 and nums[i] > nums[i-1]):
                flag = False
                right = nums[i:]
                leftV = nums[i-1]
                min = nums[i]
                for k in range(len(right)):
                    if(right[k] > nums[i-1] and min > right[k]):
                        min = right[k]
                rightV = min
                nums[i-1] = rightV

                for j in range(len(right)):
                    if rightV == right[j]:
                        nums[j+i] = leftV
                        break
                storeleft = nums[:i]
                storeright = nums[i:]
                nums.clear();
                nums += storeleft
                nums += sorted(storeright)
                break
        if flag:
            temp = list(reversed(nums))
            nums.clear()
            nums += temp

nums = [1,1,5]
Solution().nextPermutation(nums)
print(nums)


