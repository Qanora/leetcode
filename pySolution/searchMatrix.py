class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix:
            return False
        row = len(matrix)
        col = len(matrix[0])
        if row == 1 and col == 0:
            return False

        total = row * col - 1

        leftIndex = 0
        leftPosition = (0,0)
        leftV = matrix[leftPosition[0]][leftPosition[1]]

        rightIndex = total
        rightPosition = (row-1,col-1)
        rightV = matrix[rightPosition[0]][rightPosition[1]]

        midIndex = int((leftIndex + rightIndex)/2)
        midPosition = (int(midIndex/col), midIndex%col)
        midV = matrix[midPosition[0]][midPosition[1]]

        while leftIndex <= rightIndex:
            if target < midV:
                rightIndex = midIndex - 1
                rightPosition = midPosition
                rightV = midV
            if target > midV:
                leftIndex = midIndex + 1
                leftPosition = midPosition
                leftV= midV
            if target == midV:
                return True

            midIndex = int((leftIndex + rightIndex) / 2)
            midPosition = (int(midIndex / col), midIndex % col)
            midV = matrix[midPosition[0]][midPosition[1]]
            print(midIndex, midPosition, midV)

        return False

s = Solution().searchMatrix([[1]],0)
print(s)