class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # initialize the dimensions
        M, N = len(obstacleGrid), len(obstacleGrid[0])
        # a dp row
        dp = [0] * N
        # the last value being set to 1 
        dp[N - 1] = 1

        # go thru the list of rows in reverse order
        for r in reversed(range(M)):
            # go thru every col in reverse order
            for c in reversed(range(N)):
                # if the value in the grid is a 1, then we know it is blocked off
                if obstacleGrid[r][c]:
                    # dp at this column is going to be equal to 0
                    dp[c] = 0
                elif c + 1 < N:
                    dp[c] = dp[c] + dp[c + 1]

        return dp[0]
        