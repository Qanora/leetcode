class Solution:
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        if num == 1:
            return True
        while num != 1:
            flag = True
            for val in (2, 3, 5):
                if num % val == 0:
                    num //= val
                    flag = False
                if num == 1:
                    break
            if flag:
                return False
        return True

s = Solution().isUgly(8)
print(s)