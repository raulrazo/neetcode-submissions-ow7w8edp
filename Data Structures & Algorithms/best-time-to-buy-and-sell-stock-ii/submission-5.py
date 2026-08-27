class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        # start at 1 so we have a day before to compare to
        for i in range(1, len(prices)):
            # DNU: Why does prices today need to be higher than prices yesterday?
            # check's whether today's prcies are higher than
            # yesterdays.
            # if they are, then an upward price movement
            # occured between day [i - 1] and day [i].
            # meaning selling today will lead to higher gains.
            if prices[i] > prices[i - 1]:
                # so that makes us calculate a profit.
                # calculate the gain b/w today's price and
                # adds it directly to profit
                profit += (prices[i] - prices[i - 1])

        # returns the aggregated total profit after
        # scanning all days in the array. 
        return profit 


        # O(n) time complexity because we visit every price in prices list
        # O(1) space complexity because we don't require any extra memory
        