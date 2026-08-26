class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # initialize two pointers for sliding window
        # l is buy day
        l = 0

        # r is sell day
        r = 0

        # track maximum profit
        maxP = 0

        # while r is in the array
        while r < len(prices):
            # if prices at our buy day are less than
            # prices on our current sell day
            # then that means we can make a profit
            if prices[l] < prices[r]:
                # so we compute that profit and update our maxP
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)

            # if prices at our buy day are higher than
            # prices at our current sell day 
            # then we want to move our buy day
            # to the current sell day because they are lower
            # and since they are lower, that gives us a chance
            # for higher profit in the future when we decide to sell 
            # so this is shrinking our window
            else:
                l = r

            # time moves on regardless so onto the next day
            r += 1

        # return the max profit we got
        return maxP


        # O(n) time complexity because we have to iterate through the entire prices array
        # O(1) space compexity because we do not use any extra memory
        