import math


class Solution:
    def trailingZeroes(self, n):
        temp = [5]
        for _ in range(50):
            temp.append(temp[-1]*5)
        count = 0
        for i in range(len(temp)-1, -1, -1):
            if n >= temp[i]:
                count += n // temp[i]
        return count

ans = []
for i in range(1000):
    temp = math.factorial(i)
    count = 0
    while True:
        if temp % 10 == 0:
            count += 1
        else:
            ans.append(count)
            print(i, count, Solution().trailingZeroes(i))
            break
        temp = temp // 10