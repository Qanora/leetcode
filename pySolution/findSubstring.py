class Solution:
    def findSubstring(self, s, words):
        if len(words) == 0:
            return []
        l = len(words[0])
        d = {}
        for w in words:
            if w in d:
                d[w] += 1
            else:
                d[w] = 1
        i = 0
        ans = []

        for k in range(l):
            left = k
            subd = {}
            count = 0
            for j in range(k, len(s)-l+1, l):
                tword = s[j:j+l]
                if tword in d:
                    if tword in subd:
                        subd[tword] += 1
                    else:
                        subd[tword] = 1
                    count += 1
                    while subd[tword] > d[tword]:
                        subd[s[left:left+l]] -= 1
                        left += l
                        count -= 1

                    if count == len(words):
                       ans.append(left)
                else:
                    left = j + l
                    subd = {}
                    count = 0
        return ans
s = Solution()
print(s.findSubstring("barfoothefoobarman",["foo","bar"]))

