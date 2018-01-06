class Solution:
    def canCompleteCircuit(self, gas, cost):
        temp = [0] * len(gas)
        count = 0
        for i in range(len(gas)):
            temp[i] = gas[i] - cost[i]
            count += temp[i]
        if count < 0:
            return -1
        i = 0
        while i < len(temp):
            if temp[i] < 0:
                i += 1
            j = i+1
            count = temp[i]
            while j != i :
                if j >= len(temp):
                    j = 0
                if i == j:
                    break
                count += temp[j]
                if count < 0:
                    break
                j += 1
            if count < 0:
                i = j
            else:
                return i


s = Solution().canCompleteCircuit([2],[2])
print(s)