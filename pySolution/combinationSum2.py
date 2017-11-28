class Solution:
    def combinationSum2(self, candidates, target):
        candidates = sorted(candidates)
        print(candidates)
        solution =[]
        set = []
        self.solve(candidates,target,solution,set,-1)
        return set

    def solve(self,candiates, target, solution, set, nums):
        for i in range(len(candiates)):
            if i > nums:
                if candiates[i] + sum(solution) <= target:
                    solution.append(candiates[i])
                    self.solve(candiates, target, solution, set, i)
                    if sum(solution) == target:
                        if solution not in set:
                            new_solution = solution[0:]
                            set.append(new_solution)
                    solution.pop()

                if sum(solution) == target:
                    if solution not in set:
                        new_solution = solution[0:]
                        set.append(new_solution)
                        return