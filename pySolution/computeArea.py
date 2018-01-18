class Solution:
    def computeArea(self, A, B, C, D, E, F, G, H):
        if E > C or A > G or B > H or F > D:
            return 0
        x = [A,C,E,G]
        y = [B,D,F,H]
        x.sort()
        y.sort()
        return (x[2]-x[1])*(y[2]-y[1])


s = Solution().computeArea(0, 0, 0, 0, -1, -1, 1, 1)
print(s)