class Solution:
    def minimumTotal(self, triangle):
        if not triangle:
            return 0
        for i in range(len(triangle)-2,-1,-1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i+1][j+1], triangle[i+1][j])
        return triangle[0][0]

s = Solution().minimumTotal([[2],[3,4]])
print(s)