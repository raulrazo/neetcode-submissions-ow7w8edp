class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # get the dimensions
        ROWS = len(board)
        COLS = len(board[0])

        # since we cannot revisit the same character twice within our path
        # we are going to use a set to add all the current positions from our board
        # that are currently within our path
        path = set()

        # backtracking formula
        # created a nested DFS function within the regular function
        def dfs(r, c, i): # pass in the position of the board we are at and i is going to tell us the current character within our target word that we are looking for
            # if we ever reach the end of the word
            # AKA if i ever equals the last position
            if i == len(word):
                # we found the word so we can return True
                return True

            # if we go out of bounds
            if (r < 0 or c < 0 or 
                r >= ROWS or c >= COLS or 
                word[i] != board[r][c] or # if we found the wrong character then we want to return false
                (r,c) in path): # if our position is inside our path set means we are visiting it twice NONO
                return False

            # we found the character we are looking for
            # take our path and add the current position to it
            path.add((r, c))

            # we are going to run dfs in all 4 adjacent positions
            # adding 1 to i because we are looking for the next character
            res = (dfs(r + 1, c, i + 1) or
                    dfs(r - 1, c, i + 1) or
                    dfs(r, c + 1, i + 1) or
                    dfs(r, c - 1, i + 1))

            # if any of these return True then our result is going to return True
            # we only need to find our target word one single time
            
            # take path variable and remove from it the position we just added to the path
            # because we are no longer visiting that position
            # we are returning from this function call so therefore we do not need to continue to visit this bullshit
            path.remove((r,c)) 
            return res

        # dfs function is main part of backtracking problems

        # go to every single position in our grid and run this dfs function on it
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0): return True

        return False



        