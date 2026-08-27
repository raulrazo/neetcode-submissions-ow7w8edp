class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # two pointers to track buy and sell days
        # sliding window approach

        # initalize profit
        maxProfit = 0

        # initalize l pointer, r pointer will be in loop
        # l represents our buy day
        l = 0

        # iterature thru all the days
        for r in range(len(prices)):
            # profit happens when sell is > buy
            # if sell prices are higher today
            # than the day we bought
            # then we have potential new max profit
            if prices[r] > prices[l]:
                # calculate profit for this occurance
                profit = prices[r] - prices[l]
                # update profit
                maxProfit = max(maxProfit, profit)
            
            # if sell prices are lower than buy prices
            # then we update our left pointer / buy day
            # to this day at r
            # because this gives us a new low that we can
            # buy at and this can give a higher profit
            # when we find a day to sell
            else:
                l = r

        # return max profit
        return maxProfit

        