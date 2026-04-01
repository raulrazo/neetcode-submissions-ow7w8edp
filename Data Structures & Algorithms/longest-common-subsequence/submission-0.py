class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # create 2D grid and set it to all 0s
        # + 1 is for the outer layer of 0s
        # dimensions are based on the size of the 2 strings
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

        # iterate thru this 2D grid in reverse order
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                # if the chars in both strings match each other
                if text1[i] == text2[j]:
                    # then at this position, we can take 1 
                    # + the diagonal(i+1, j+1)
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    # they don't match so we take the max 
                    # b/w the right value and the bottom value
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])

        # result is at top left of matrix
        return dp[0][0]
        