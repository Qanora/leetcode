class Solution:
    def addBinary(self, a, b):
        return bin(int(a,2)+int(b,2))[2:]

s = Solution().addBinary("11","11")
print(s)