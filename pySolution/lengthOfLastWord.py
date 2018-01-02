class Solution:
    def lengthOfLastWord(self, s):
        v = s.split(" ")
        for i in range(len(v)):
            if len(v[-1-i]) != 0:
                return len(v[-1-i])
        return len(v[-1])

s = Solution().lengthOfLastWord("Today is a nice day ")
print(s)