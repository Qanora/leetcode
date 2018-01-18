class Solution:
    def findOrder(self, numCourses, prerequisites):
        incLinkCounts = [0]*numCourses
        adjs = [[] for _ in range(numCourses)]
        self.initialiseGraph(incLinkCounts, adjs, prerequisites, numCourses)
        return self.solveByBFS(incLinkCounts, adjs)

    def initialiseGraph(self, incLinkCounts, adjs, prerequisites, numCourses):
        for val in prerequisites:
            incLinkCounts[val[0]] += 1
            adjs[val[1]].append(val[0])

    def solveByBFS(self, incLinkCounts, adjs):
        order = []
        toVisit = []
        for i in range(len(incLinkCounts)):
            if incLinkCounts[i] == 0:
                toVisit.append(i)
        while toVisit:
            From = toVisit.pop(0)
            order.append(From)
            for to in adjs[From]:
                incLinkCounts[to] -= 1
                if incLinkCounts[to] == 0:
                    toVisit.append(to)
        return order if len(order) == len(incLinkCounts) else []


s = Solution().findOrder(2, [[1,0]])
print(s)