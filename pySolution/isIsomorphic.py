class Solution:
    def isIsomorphic(self, s, t):
        dict = {}
        temp = []
        for i in range(len(s)):
            if t[i] not in dict:
                dict[t[i]] = s[i]
                if s[i] not in temp:
                    temp.append(s[i])
                else:
                    return False
            else:
                if dict.get(t[i]) != s[i]:
                    return False
        return True

s = Solution().isIsomorphic("ab","ca")
print(s)
