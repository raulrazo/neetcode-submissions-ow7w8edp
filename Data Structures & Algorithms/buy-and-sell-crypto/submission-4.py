class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        l = 0
        r = 1

        while r < len(prices):
            profit = prices[r] - prices[l]
            maxP = max(maxP, profit)

            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r

            r += 1


        return maxP

        