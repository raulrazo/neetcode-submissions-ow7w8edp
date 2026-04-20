class Solution:
    def countBits(self, n: int) -> List[int]:
        # initialize dp array
        dp = [0] * (n + 1)

        # keep track of highest power of 2 so far
        offset = 1

        for i in range(1, n + 1):
            # can we double our offset?
            if offset * 2 == i:
                # update our offset
                offset = i
            
            # compute the number of 1s in i's binary representation
            dp[i] = 1 + dp[i - offset]

        # dp is our answer array
        return dp

        