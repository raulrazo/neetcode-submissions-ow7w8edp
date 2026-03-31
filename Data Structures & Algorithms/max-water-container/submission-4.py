class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # area = r - l * min(heights[l], heights[r])
        maxA = 0
        l = 0
        r = len(heights) - 1

        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            maxA = max(maxA, area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return maxA 
        