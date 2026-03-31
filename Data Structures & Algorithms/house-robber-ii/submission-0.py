class Solution:
    def rob(self, nums: List[int]) -> int:

        # skip the first house and last house
        # edge case: we get only 1 house and the max ends up being 0, that's why we have nums[0]
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))





    # solution from house robber 1
    def helper(self, nums):
        # these store the max amount you can rob from the previous two houses
        rob1, rob2 = 0, 0

        # go thru every house
        for n in nums:
            # rob1 + n b/c we have to skip rob2 b/c adjacent
            # same concept for rob2
            newRob = max(rob1 + n, rob2)

            # shift rob1 and rob2
            rob1 = rob2
            rob2 = newRob

        # rob2 will contain the max
        return rob2
        