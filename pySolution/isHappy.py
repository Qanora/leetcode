class Solution:
    def isHapply(self, n):
        temp = 0
        stack = [n]
        while n:
            temp += pow(n%10, 2)
            n //= 10
            if n == 0:
                n = temp
                if n == 1:
                    return True
                if n not in stack:
                    stack.append(n)
                else:
                    return False
                temp = 0

s = Solution().isHapply(19)
print(s)