class Solution:
    def generateMatrix(self, n):
        temp = [[(j,i) for i in range(n)] for j in range(n)]
        ans = [ [0] * n for _ in range(n)]
        ret = []
        while temp:
            ret += temp.pop(0)
            if temp and temp[0]:
                for row in temp:
                    ret.append(row.pop())
            if temp:
                ret += temp.pop()[::-1]
            if temp and temp[0]:
                for row in temp[::-1]:
                    ret.append(row.pop(0))
        count = 1
        for i in ret:
            ans[i[0]][i[1]] = count
            count += 1
        return ans
s = Solution().generateMatrix(3)
print(s)