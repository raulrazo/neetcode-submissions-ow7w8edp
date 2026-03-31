class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp array
        # amount + 1 because we are going from 0... amount
        dp = [amount + 1] * (amount + 1)

        # base case
        dp[0] = 0

        # start computing every value in dp
        # reverse order
        # for every amount
        for a in range(1, amount + 1):
            # for every coin
            for c in coins:
                # if this is positive than that means we can continue searching
                if a - c >= 0:
                    # we possibly found a solution for our dp
                    # 1 comes from current coin c
                    # dp[a - c] comes from shit like this: dp[7] = 1 + dp[3]
                    # this is the recurrence relation
                    dp[a] = min(dp[a], 1 + dp[a - c])

        # if is for edge case where we couldn't compute the amount
        return dp[amount] if dp[amount] != amount + 1 else - 1

        