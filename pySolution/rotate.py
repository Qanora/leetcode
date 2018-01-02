class Solution:
    def rotate(self, matrix):
        """ij
        [00,01,02]
        [10,11,12]
        [20,21,22]

        [00,01,02,10,11,12,20,21,22] for i in len(matrix) for j in len(martrix[1]) ij
        [20,10,00,21,11,01,22,12,02] for l in len(matrix) for k in len(martrix[1], 0 -1) kl
        lk
        [20,10,00]
        [21,11,01]
        [22,12,02]
        table = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]"""
        ans = []
        temp = []
        count = 0
        for i in range(len(matrix)):
            for j in range(len(matrix)-1, -1, -1):
                temp.append(matrix[j][i])
                count += 1
                if count == len(matrix):
                    count = 0
                    ans.append(temp[:])
                    temp = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix[i][j] = ans[i][j]

s = [[1,2,3],[4,5,6],[7,8,9]]
Solution().rotate(s)
print(s)

