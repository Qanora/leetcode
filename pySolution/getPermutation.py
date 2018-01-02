import math
class Solution:
    def getPermutation(self, n, k):
        if n == 1 and k == 1:
            return str(1)
        ans = [x for x in range(1,n+1)]
        print(ans)
        strs = ""
        k = k - 1
        while len(ans) > 2 :
            temp = int(math.floor(math.factorial(n)/n))
            print("temp ", temp)
            position = int(math.floor(k/temp))
            print("position ", position)
            k = k - temp * position
            print("k ", k)
            strs += str(ans[position])
            ans.pop(position)
            n = n - 1
        strs += str(ans.pop(k))
        strs += str(ans.pop())
        return strs

Solution().getPermutation(3,6)