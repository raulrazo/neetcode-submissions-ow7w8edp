class Solution:
    def rob(self, nums: List[int]) -> int:
        # we only need to maintain the last two maxes we can rob from
        # b/c memoization or something
        rob1, rob2 = 0, 0

        # iterate thru each of the houses
        for n in nums:
            # compute the max we can rob up until this value n
            # [rob1, rob2, n, n + 1, ...]
            temp = max(n + rob1, rob2)

            # update rob1 to now = rob2, aka shifting them
            rob1 = rob2

            rob2 = temp

        # return rob2 b/c by the the time we get to the end
        # rob2 will be equal to the last value meaning it 
        # will be the max we can rob from all the houses
        return rob2
        