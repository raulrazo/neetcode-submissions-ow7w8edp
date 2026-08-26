class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # initialize up, down, left, right directions
        # for exploring neighboring cells
        directions = [
            [1, 0],
            [-1, 0],
            [0, 1],
            [0, -1]
        ]

        # initialize rows and cols
        ROWS = len(grid)
        COLS = len(grid[0])

        # initialize island count
        islands = 0

        # define bfs function
        # pass in row and column as position 
        def bfs(r, c):
            # intialize doubly ended queue
            q = deque()

            # mark this visited cell as water
            # so it doesn't have the chance to count
            # as another island after this
            grid[r][c] = "0"

            # add this node to the back of our queue
            q.append((r, c))

            # while our q is not empty,
            while q:
                # get our node's position 
                # and pop it from our queue
                row, col = q.popleft()

                # and we search all of our nodes neighbors
                for dr, dc in directions:
                    # update our search position
                    nr = dr + row
                    nc = dc + col

                    # if this new position is out of bounds
                    # or if it is water, meaning we already marked it / visited it
                    # DNU: why check if it is water? 
                    if (nr < 0 or nc < 0 or nr >= ROWS or
                        nc >= COLS or grid[nr][nc] == "0"):

                        # if it is those things, then we move past it
                        # DNU: why move past it?
                        continue 

                    # if this node at neighboring position
                    # is a '1' so it is part of our current island
                    # then we push it to the back of our queue
                    # DNU: why push it to queue?
                    q.append((nr, nc))

                    # and then we mark it as water to 
                    # show that it is visited
                    # and won't get picked up by any other things

                    # DNU: why mark it as water?
                    grid[nr][nc] = "0"

        # for every position on this grid
        # we run BFS on it if it is a '1'
        # meaning we have found a new island
        # so this is really about finding unique islands
        # and marking all their land as water when we find them
        # so we know that when we hit a new '1', 
        # then it is confirmed to be a new unique island
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    bfs(r,c)
                    islands += 1

        return islands


        