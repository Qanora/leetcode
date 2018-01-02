class Solution:
    def restoreIpAddresses(self, s):
        if not s:
            return []
        if len(s) > 12:
            return []
        self.ans = []
        self.dfs(s, 0, [])
        rAns = []
        for temp in self.ans:
            v = ""
            for val in temp:
                v += val
                v += "."
            rAns.append(v[0:len(v)-1])
        return rAns

    def dfs(self, s, deep, temp):
        if not s or deep >= 3:
            if s[0] == '0' and len(s) != 1:
                return
            if int(s) > 255:
                return
            temp.append(s)
            self.ans.append(temp[:])
            temp.pop()
            return
        else:
            for i in range(1,4):
                if s[0] == '0' and i != 1:
                    continue
                if int(s[0:i]) > 255:
                    continue
                temp.append(s[0:i])
                if s[i:]:
                    self.dfs(s[i:], deep + 1, temp)
                temp.pop()


s = Solution().restoreIpAddresses("010010")
print(s)