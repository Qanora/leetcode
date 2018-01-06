class Solution:
    def candy(self, ratings):
        temp = [1] * len(ratings)
        for i in range(len(ratings)-1):
            if ratings[i] < ratings[i+1]:
                if temp[i] >= temp[i+1]:
                    temp[i+1] = temp[i] + 1

        for i in range(len(ratings)-1,0,-1):
            if ratings[i-1] > ratings[i]:
                if temp[i-1] <= temp[i]:
                    temp[i-1] = temp[i] + 1

        count = 0
        print(temp)
        for val in temp:
            count += val
        return count

s = Solution().candy([3,2,1])
print(s)
