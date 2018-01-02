class Interval:
    def __init__(self, s = 0, e = 0):
        self.start = s
        self.end = e
class Solution:
    def insert(self, intervals, newInterval):
        ans = []
        intervals.append(newInterval)
        for i in sorted(intervals, key=lambda x: x.start):
            if ans and ans[-1].end >= i.start:
                ans[-1].end = max(i.end, ans[-1].end)
            else:
                ans.append(i)
        return ans

input = [[1,5]]
inputInterval = [Interval(x[0],x[1]) for x in input]
inputNewInterval = Interval(5,7)
s = Solution().insert(inputInterval,inputNewInterval)
for i in s:
    print(i.start, i.end)