class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        # start at 1 so we have a day before to compare to
        for i in range(1, len(prices)):
            # DNU: Why does prices today need to be higher than prices yesterday?
            # A-DNU: b/c a trade only makes money if the sell price is higher than the buy price
            # check's whether today's prcies are higher than
            # yesterdays.
            # if they are, then an upward price movement
            # occured between day [i - 1] and day [i].
            # meaning selling today will lead to higher gains.
            if prices[i] > prices[i - 1]:
                # so that makes us calculate a profit.
                # calculate the gain b/w today's price and
                # adds it directly to profit.
                # DNU: Why running profit?
                # A-DNU: We have a running profit b/c say prices increase over 4 days.
                # So p1 < p2 < p3 < p4.
                # You could hold on p1 and then sell on p4
                # and make a profit.
                # But since we can sell AND buy on the same day here
                # then we could also do this: buy p1 -> sell p2; buy p2 -> sell p3; buy p3 -> sell p4
                # and this gives us the same profit as holding
                # it for all of those days.
                # having a running sum maximizes our
                # profit b/c it's the same outcome as
                # holding BUT if there is no gain 
                # for the next day, then we can still
                # hold and wait for a day where there 
                # is gain and maximize profit in that
                # way too.
                profit += (prices[i] - prices[i - 1])

        # returns the aggregated total profit after
        # scanning all days in the array. 
        return profit 


        # O(n) time complexity because we visit every price in prices list
        # O(1) space complexity because we don't require any extra memory
        