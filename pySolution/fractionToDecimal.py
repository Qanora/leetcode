class Solution:
    def fractionToDecimal(self, numerator, denominator):
        res = ""
        if numerator * denominator < 0:
            res += "-"
            numerator *= -1
        if numerator == 0:
            return "0"
        res += str(numerator // denominator)
        if numerator % denominator == 0:
            return res
        numerator %= denominator
        res += "."
        table = {}
        while numerator:
            if numerator not in table:
                table[numerator] = len(res)
                numerator *= 10
                res += str(numerator // denominator)
                numerator = numerator % denominator
            else:
                return res[:table[numerator]] + "(" + res[table[numerator]:] + ")"
        return res

s = Solution().fractionToDecimal(-50,8)
print(s)