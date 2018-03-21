import re

class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        print(bin(n)[2:])
        digit = "0" + bin(n)[3:]
        print(digit)
        pattern = "(1{2,})0"
        count = 0
        digit = digit[::-1]
        while re.search(pattern, digit):
            digit = re.sub(pattern, lambda m: len(m.group(1))*"0"+"1", digit,1)
            count += 1
            print(digit)
        if digit[0] == "0":
            digit = digit[1:]
        print(digit)
        for val in digit:
            if val == "1":
                count += 2
            else:
                count += 1
        return count






s = Solution().integerReplacement(3)
print(s)