import math


class Solution:
    def climbStairs(self, n):
        return int((pow((1+math.sqrt(5))/2,n+1)-pow((1-math.sqrt(5))/2,n+1))/math.sqrt(5))
