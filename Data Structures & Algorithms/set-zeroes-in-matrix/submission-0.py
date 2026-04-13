class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # get rows and cols variables
        ROWS, COLS = len(matrix), len(matrix[0])

        # extra variable to tell us if the first row is 0 or not
        rowZero = False

        # determine which rows/cols need to be zero
        # iterate thru every cell
        for r in range(ROWS):
            for c in range(COLS):
                # if we find a 0
                if matrix[r][c] == 0:
                    # we set the first value in this column to 0
                    matrix[0][c] = 0
                    # only going to do this if not top left position
                    # b/c we have dedicated rowZero value for it
                    if r > 0:
                        # we set the first value in this row to 0
                        matrix[r][0] = 0
                    else:
                        rowZero = True

        # now we zero them out
        # skip first row and col 
        for r in range(1, ROWS):
            for c in range(1, COLS):
                # if first row value is 0
                # or if the first column value is 0
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    # set the current position we are at to 0
                    matrix[r][c] = 0

        # zero out first row and col if we need to
        if matrix[0][0] == 0:
            # set every value in the first col to 0
            for r in range(ROWS):
                matrix[r][0] = 0

        if rowZero:
            # zero out every value in the first one
            for c in range(COLS):
                matrix[0][c] = 0

        
        