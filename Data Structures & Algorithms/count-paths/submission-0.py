class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # initialize bottom row
        # and we know it is going to be all 1s
        row = [1] * n

        # go thru all rows except for the last one
        for i in range(m - 1):
            # for each row we compute the new row
            newRow = [1] * n

            # to avoid edge case of having to check out of bounds
            # we go thru every column except the rightmost column
            # b/c we know the rightmost column is always going to be 1
            # n - 2 = second to last position
            # -1 = go until we get to beginning
            # -1 = go in reverse order
            for j in range(n - 2, -1, -1):
                # compute new position value
                # newRow[j + 1] = right value
                # row[j] = down value
                newRow[j] = newRow[j + 1] + row[j]

            # update old row to new row
            row = newRow

        # return top left value
        return row[0]

        # O(n * m) time
        # O(n) space b/c that's the length of a row


        