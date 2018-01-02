class Solution:
    def multiply(self, num1, num2):
        ans = []
        num1 = num1[::-1]
        num2 = num2[::-1]
        maxLen = 0
        finalAns = []
        for i in range(len(num1)):
            temp = []
            for _ in range(i):
                temp.append(0)
            for j in range(len(num2)):
                temp.append(int(num1[i])*int(num2[j]))
            ans.append(temp)
        for i in range(len(ans)):
            maxLen = max(maxLen, len(ans[i]))

        temp = 0
        next_temp = 0
        for i in range(maxLen):
            next_temp = 0
            for j in range(len(ans)):
                if len(ans[j]) > i:
                    temp += ans[j][i]
            while(temp > 9):
                temp -= 10
                next_temp += 1
            finalAns.append(temp)
            temp = next_temp
        if next_temp != 0:
            finalAns.append(next_temp)
        strs = ""
        flag = True
        for i in range(len(finalAns)):
            if finalAns[::-1][i] != 0:
                flag = False
            strs += str(finalAns[::-1][i])
        if flag:
            return "0"
        return strs




s = Solution().multiply("0","1000")
print(s)
