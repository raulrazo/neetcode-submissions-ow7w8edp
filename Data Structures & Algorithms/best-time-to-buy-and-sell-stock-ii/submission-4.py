class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i in range(1, len(prices)):
            # DNU: Why does prices today need to be higher than prices yesterday?
            if prices[i] > prices[i - 1]:
                profit += (prices[i] - prices[i - 1])

        return profit 


        # O(n) time complexity because we visit every price in prices list
        # O(1) space complexity because we don't require any extra memory
        