class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        ans = [1,0,1,1,0]
        if n <= 4:
            return ans[n]
        for i in range(5,n+1):
            if min(ans[-1],ans[-2],ans[-3]) == 0:
                ans.append(1)
            else:
                ans.append(0)
        return True if ans[-1] == 1 else False
Solution().canWinNim(10)