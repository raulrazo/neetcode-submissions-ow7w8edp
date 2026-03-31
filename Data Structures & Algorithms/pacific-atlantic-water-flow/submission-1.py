class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])

        # two hashsets for visited schpots
        pac = set()
        atl = set()

        def dfs(r, c, visit, prevHeight):
            # if this position has already been visited or out of bounds
            # gotta check if height is smaller than
            if ((r,c) in visit or 
                r < 0 or c < 0 or r == ROWS or c == COLS or
                heights[r][c] < prevHeight):
                return

            # adding a new cell
            visit.add((r,c))

            # run dfs on all 4 of its neighbors
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])


        # then go thru every single position in the first row
        # for column in the first row
        for c in range(COLS):
            # run a dfs on this position
            # 0 for the first row
            # pass in visit set for pacific because this is for the pacific ocean
            # height so we make sure we are allowed to visit that cell
            dfs(0, c, pac, heights[0][c])

            # let's go thru every position in the last row as well
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

        # now we do it for the columns
        for r in range(ROWS):
            # for pacific
            dfs(r, 0, pac, heights[r][0])

            # for atlantic
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        # once these two loops have executed we will have marked every single position 
        # that can reach position and atlantic

        # now we go thru every single position in the grid
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    # if this position was in both pacific and atlantic then we want to add it to our result
                    res.append([r, c])

        return res



        