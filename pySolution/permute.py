class Solution:
    def permute(self, nums):
        if not nums:
            return [[]]
        x = nums[0]
        xs = nums[1:]
        temp = self.permute(xs)
        fianl = []
        for i in temp:
            fianl.extend(self.insert(x,i))
        return fianl

    def insert(self, n, nums):
        temp = []
        result = []
        if not nums:
            temp.append(n)
            result.append(temp[:])
            return result[:]
        else:
            nF = nums[0]
            nL = nums[1:]
            temp4 = []
            temp4.append(n)
            temp4.append(nF)
            temp4.extend(nL)
            result.append(temp4)
            temp3 = self.insert(n,nL)
            for i in temp3:
                temp2 = []
                temp2.append(nF)
                temp2.extend(i)
                result.append(temp2[:])
            return result


import math


class Solution:
    def allPermutations(l):
        if len(l) <= 1:
            print(l)
            yield l
        else:
            for element in Solution.allPermutations(l[1:]):
                print("solution.all ", Solution.allPermutations(l[1:]))
                print("element ",element)
                print("l ",l)
                for i in range(len(l)):
                    print("element[:1] ", element[:i], "l[0:1] ", l[0:1], "element[i:] ", element[i:])
                    yield element[:i] + l[0:1] + element[i:]

    def permute(self, nums):
        r, n, p = [], 0, Solution.allPermutations(nums)
        while n < math.factorial(len(nums)):
            r.append(next(p))
            n += 1
        return r


s = Solution().permute([1,2,3])
w = [1,2,3]
print(w[:0])
print(s)

s = Solution()
p = s.permute([1,2,3,4])
print(len(p))
