class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # get the dimensions of the matrix
        ROWS = len(matrix)
        COLS = len(matrix[0])

        # same size of matrix but we are adding dummy outer layer
        self.sumMat = [[0] * (COLS + 1) for r in range(ROWS + 1)]

        # go thru every position
        for r in range(ROWS):
            # calculate prefix sum for each row
            prefix = 0
            for c in range(COLS):
                prefix += matrix[r][c]

                # rectangle that is directly above this one
                above = self.sumMat[r][c + 1]

                # update sumMat at this position but offset by 1 because of dummy layer
                # value will be prefix sum + whatever rectangle is above this position
                self.sumMat[r + 1][c + 1] = prefix + above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # r1 and c1 define top left
        # r2 and c2 define bottom right

        # add 1 to all of them because of offset
        row1 += 1
        col1 += 1
        row2 += 1
        col2 += 1
        
        # get the area of 4 rectangles
        bottomRight = self.sumMat[row2][col2]

        above = self.sumMat[row1 - 1][col2]

        left = self.sumMat[row2][col1 - 1]

        topLeft = self.sumMat[row1 -1][col1 - 1]

        return bottomRight - above - left + topLeft



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)