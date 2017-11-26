class Solution:
    def countAndSay(self,n):
        str = "1"
        while(n > 1):
            n = n - 1
            str = self.count(str)

        return str

    def count(self, strs):
        new_strs = ""
        count = 0
        a = strs[0]
        for i in range(len(strs)):
            if a == strs[i]:
                count = count + 1
            else:
                new_strs = new_strs + str(count) + a
                a = strs[i]
                count = 1
        new_strs = new_strs + str(count) + strs[-1]
        return new_strs

n = Solution().countAndSay(2)
print(n)

