import math


class Solution:
    def countPrimes(self, n):
        count = 0
        for i in range(n):
            if self.isPrimes(i):
                count += 1
        return count

    def isPrimes(self, n):
        if n < 2:
            return False
        for i in range(2,int(math.sqrt(n))+1):
            if n % i == 0:
                return False
        return True
Solution().countPrimes(6)