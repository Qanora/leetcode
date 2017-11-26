class Solution:
    def combinationSum(self, candidates, target):
        solution =[]
        set = []
        self.solve(candidates,target,solution,set,0)
        return set

    def solve(self,candiates, target, solution, set, nums):
        for i in range(len(candiates)):
            if i >= nums:
                if sum(solution) == target:
                    if solution not in set:
                        new_solution = solution[0:]
                        set.append(new_solution)
                        return

                if candiates[i] + sum(solution) <= target:
                    solution.append(candiates[i])
                    self.solve(candiates, target, solution, set, i)
                    solution.pop()



s = Solution().combinationSum([1,2],3)
print(s)

