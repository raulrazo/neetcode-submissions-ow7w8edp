class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # get the dimensions of the grid
        M, N = len(obstacleGrid), len(obstacleGrid[0])

        # use a hashmap to use as our cache 
        # and we initialize the bottom right position to be 1 because that is our base case
        dp = {(M - 1, N - 1): 1}

        # recursive function 
        def dfs(r, c):
            # base case 1 and 2: we go out out bounds with row or col
            # base case 3: the grid position value is a 1 so it is block and we can't traverse through there
            if r == M or c == N or obstacleGrid[r][c]:
                return 0

            # this is the case if we have already computed the value at this position
            # and it is in our cache
            if (r, c) in dp:
                return dp[(r, c)]

            # do recursion here and count the paths at row + 1 and col + 1

            dp[(r, c)] = dfs(r + 1, c) + dfs(r, c + 1)
            return dp[(r, c)]

        return dfs(0, 0)
        