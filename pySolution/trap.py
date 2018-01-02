class Solution:
    def comfortment(self, height):

        n = len(height)
        l, r, minHeight, maxHeight = 0, n - 1, 0, 0
        ans = [1 for _ in height]
        while l < r:
            while l < r and height[l] <= minHeight:
                if minHeight - height[l] != 0:
                    ans[l] = 0
                l += 1
            while r > l and height[r] <= minHeight:
                if minHeight - height[r] != 0:
                    ans[r] = 0
                r -= 1
            maxHeight = height.index(max(height[l], height[r]))
            minHeight = min(height[l], height[r])
        ans[maxHeight] = 2
        return ans

Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1])