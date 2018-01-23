class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        temp = bin(n)[2:]
        if n == 0:
            return False
        if temp[0] == '1':
            if len(temp) == 1:
                return True
            else:
                for val in temp[1:]:
                    if val != '0':
                        return False
                return True
        return False

for val in range(100):
    s = Solution().isPowerOfTwo(val)
    print(val,s)