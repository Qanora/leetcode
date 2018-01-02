class Solution:
    def largestRectangleArea(self, heights):
        l =  len(heights)-1
        ans = [[0,l]]
        temp = []
        for i, v in enumerate(heights):
            temp.append((i,v))
        maxR = 0
        for val in sorted(temp,key=lambda x:x[1]):
            for i in range(len(ans)):
                if ans[i][0] < val[0] and ans[i][1] > val[0]:
                    maxR = max(maxR, (ans[i][1] - ans[i][0] + 1) * val[1])
                    ans.append([ans[i][0], val[0]-1])
                    ans.append([val[0]+1, ans[i][1]])
                    ans.pop(i)
                    break
                elif ans[i][0] == val[0] and ans[i][1] == val[0]:
                    maxR = max(maxR, val[1])
                    ans.pop(i)
                    break
                elif ans[i][0] == val[0] and ans[i][1] != val[0]:
                    maxR = max(maxR, (ans[i][1] - ans[i][0] + 1) * val[1])
                    ans.append([ans[i][0] + 1, ans[i][1]])
                    ans.pop(i)
                    break
                elif ans[i][0] != val[0] and ans[i][1] == val[0]:
                    maxR = max(maxR, (ans[i][1] - ans[i][0] + 1) * val[1])
                    ans.append([ans[i][0], ans[i][1] - 1])
                    ans.pop(i)
                    break
        return maxR

s = Solution().largestRectangleArea([4,2])
print(s)