class Solution:
    def isMatch(self, s, p):
        table = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        table[0][0] = True
        for i in range(len(p)):
            if p[i] == '*' and table[0][i]:
                table[0][i+1] = True

        for i in range(len(s)):
            for j in range(len(p)):
                if p[j] == '?':
                    table[i+1][j+1] = table[i][j]
                if s[i] == p[j]:
                    table[i+1][j+1] = table[i][j]
                if p[j] == '*':
                    if i == 2 and j == 4:
                        print(table[i][j+1],table[i+1][j],table[i+1][j-1])
                    table[i+1][j+1] = table[i][j+1] or table[i+1][j]
        return table[len(s)][len(p)]

Solution().isMatch("aaaa","a*")