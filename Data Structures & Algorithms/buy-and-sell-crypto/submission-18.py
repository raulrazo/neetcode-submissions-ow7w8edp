class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        maxP = 0

        for r in range(len(prices)):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r 

        return maxP
        