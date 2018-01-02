class Solution:
    def generate(self, numRows):
        if numRows == 0:
            return []
        if numRows == 1:
            return [1]
        ans = [[1], [1, 1]]
        if numRows == 2:
            return ans
        while numRows >= 3:
            temp = [1]
            for i in range(1,len(ans[-1])):
                temp.append(ans[-1][i-1]+ans[-1][i])
            temp += [1]
            ans.append(temp[:])
            numRows -= 1
        return ans
        1
s = Solution().generate(3)
print(s)