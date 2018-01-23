class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        l = [0,0]
        r = [len(matrix)-1, len(matrix[0])-1]
        while l[0] <= r[0] and l[1] <= r[1]:
            if target in (matrix[l[0]+1][l[1]+1], matrix[l[0]][l[1]+1], matrix[l[0]+1][l[1]],
                          matrix[r[0]-1][r[1]-1], matrix[r[0]][r[1]-1], matrix[r[0]-1][r[1]]):
                return True
            if matrix[l[0]+1][l[1]+1] < target:
                l[0], l[1] = l[0] + 1, l[1] + 1
            elif matrix[]

ans = [[1,3,5,7,9],[2,4,6,8,10],[11,13,15,17,19],[12,14,16,18,20],[21,22,23,24,25]]
s = Solution().searchMatrix(ans, 13)
print(s)