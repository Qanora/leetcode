class Solution:
    def plusOne(self, digits):
        num = 0
        for val in digits:
            num = num*10 + val
        num = num + 1
        ans = str(num)
        rAns = []
        for v in ans:
            rAns.append(int(v))
        return rAns
s = Solution().plusOne([1,0])
print(s)