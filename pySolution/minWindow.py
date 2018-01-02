import collections


class Solution:
    def minWindow(self, s, t):
        count = collections.Counter(t)
        missing = len(t)
        i, I, J = 0, 0, 0
        for j, v in enumerate(s,1):
            missing -= count[v] > 0
            count[v] -= 1
            if not missing:
                while i < j and count[s[i]] < 0:
                    count[s[i]] += 1
                    i += 1
                if not J or J - I >= j - i:
                        J ,I = j, i
        return s[I:J]
s = Solution().minWindow("a","a")
print(s)