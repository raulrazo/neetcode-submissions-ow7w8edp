class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # intialize hashmap for memoization
        # memoization = 

        # keys are tuples (i, buying) that represent 
        # unique subproblem states.
        # values store the max profit obtainable starting
        # from that state.
        dp = {}

        # defines a nested recursive helper function
        # i tracks the current trading day
        # buy = True means we can buy or wait
        # buy = False means we are holding and call sell or wait
        def dfs(i, buying):
            # base case for boundary checking
            # means we exceed prices array and
            # no further transactions can take place
            if i >= len(prices):
                return 0

            # cache lookup, checks if the subproblem
            # for (i, buying) has already been computed
            if (i, buying) in dp:
                # immediately returns the cached result,
                # pruning duplicate recursive branches.
                return dp[(i, buying)]

            # this checks the pass/idle choice for this day
            # by skipping trading on this day i and going to next
            cooldown = dfs(i + 1, buying)

            # check if we are looking to buy stock
            if buying:
                # calculate the profit if we buy today
                # this is the same as:
                # prices[r] - prices[l] where r is next day
                buy = dfs(i + 1, not buying) - prices[i]

                # selects optimal choice b/w buying today or passing today
                # storing it in our dp cache
                dp[(i, buying)] = max(buy, cooldown)

            # buying is false, meaning we are holding and can sell
            else:
                # calculates profit if we sell today
                # add prices[i] which is cash earned from selling today
                # jumps 2 days ahead because day i + 1
                # is locked out by mandatory cooldown?
                
                # inverts buying back to True
                # ready to buy again on day i + 2
                sell = dfs(i + 2, not buying) + prices[i]

                # selects optimal choice b/w selling or holding
                dp[(i, buying)] = max(sell, cooldown)

                
            return dp[(i, buying)]

        return dfs(0, True)
        

        