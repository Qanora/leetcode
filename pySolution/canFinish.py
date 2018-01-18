class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = [[] for _ in range(numCourses)]
        degrees = [0] * numCourses
        for course, prereq in prerequisites:
            degrees[prereq] += 1
            graph[course].append(prereq)

        queue = []
        count = 0
        for i in range(len(degrees)):
            if not degrees[i]:
                queue.append(i)
                count += 1

        while queue:
            course = queue.pop(0)
            for prereq in graph[course]:
                degrees[prereq] -= 1
                if degrees[prereq] == 0:
                    queue.append(prereq)
                    count += 1

        return count == numCourses
s = Solution().canFinish(4,[[1,2],[2,3]])
print(s)