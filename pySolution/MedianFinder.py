import heapq
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.ans = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        heapq.heappush(self.ans, num)
        print(self.ans)
    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.ans) %2 == 1:
            return self.ans[(len(self.ans)-1)//2]
        else:
            return (self.ans[(len(self.ans)//2)] + self.ans[len(self.ans)//2-1])/2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

s = MedianFinder()
s.addNum(-1)
s.addNum(-2)
print(s.findMedian())
s.addNum(-3)
print(s.findMedian())