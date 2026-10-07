class Solution:
    def trap(self, height: List[int]) -> int:
        # handles the edge case where the input list is empty
        if not height:
            return 0

        # initialize two pointers
        l = 0
        r = len(height) - 1

        # tracks the tallest wall encountered from the left up
        # to l and from the right down to r.
        leftMax = height[l]
        rightMax = height[r]

        res = 0

        while l < r:
            # checks which side is currently the bottleneck. 
            # b/c leftMax < rigthMax, the amount of trapped 
            # water on index l + 1 is bounded by leftMax, 
            # regardless of any taller walls further to the
            # right.
            if leftMax < rightMax:
                # advances the left pointer inward by 1
                l += 1

                # updates leftmax if the new bar (height[l])
                # is taller than previous leftMax.
                leftMax = max(leftMax, height[l])

                # calculates water trapped directly above index l
                res += leftMax - height[l]
            else:
                # vice versa
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]

        # all valid intermediate positions have been evaluated
        return res