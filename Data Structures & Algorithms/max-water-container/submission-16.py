class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # initialize two pointers
        # one at the start of container, one at the end
        l = 0
        r = len(heights) - 1

        res = 0

        while l < r:
            # calculates the capacity of the current container
            area = min(heights[l], heights[r]) * (r - l)

            # update res
            res = max(res, area)

            # greedy pointer shift
            # moving the taller boundary inward can only decrease
            # the containeter size, so the container height
            # remains bounded by the shorter line,
            # therefore the only path to a larger container is 
            # to seek a taller boundary to replace the limiting 
            # shorter side so we shift the shorter point inward
            # for that potential new find.
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1

        return res

        # Time and Space Complexity

        # O(n) time because we have to iterate through all heights
        
        # O(1) space complexity because we do not use extra memory