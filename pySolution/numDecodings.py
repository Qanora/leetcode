import math


class Solution:
    def numDecodings(self, s):
        ans = []
        for i in range(1,len(s)):
            if (int(s[i-1] + s[i]) >= 13 and int(s[i-1] + s[i]) < 20) or (int(s[i-1] + s[i]) >= 23 and int(s[i-1] + s[i]) <= 26):
                ans.append(2)
            if int(s[i-1] + s[i]) == 20 or int(s[i-1] + s[i]) == 10:
                ans.append(1)
        cur_m = 0
        for i in range(len(s)):
            if int(s[i]) >=3 and int(s[i]) <=9:
                ans.append(1)
            if int(s[i]) >= 1 and int(s[i]) <= 2:
                cur_m += 1
            elif int(s[i]) == 0:
                cur_m -= 1
                if cur_m != 0:
                    ans.append(self.fibonacci(cur_m+1))
                    cur_m = 0
            else:
                if cur_m > 1:
                    ans.append(self.fibonacci(cur_m+1))
                cur_m = 0
        if cur_m:
            ans.append(self.fibonacci(cur_m+1))
        rAns = 1
        if not ans:
            return 0
        for i in ans:
            rAns *= i
        return rAns

    def fibonacci(self,n):
        return int(1/math.sqrt(5)*(pow((1+math.sqrt(5))/2,n)-pow((1-math.sqrt(5))/2,n)))


s = Solution()
w = s.numDecodings("10")
print(w)