class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # tracks the largest rectangular area found so far.
        maxArea = 0

        # intializes a monotonic strictly increasing stack.
        # each entry stores a tuple (start_index, height).
        # start_index represents the leftmost index from
        # which a rectangle of this height could have started
        # and extended continuously to the right.
        stack = []

        # iterate thru each bar left to right.
        for i, h in enumerate(heights):
            # assumts curr bar of height h can only begin
            # at index i, if taller bars precede it, this start
            # point will be pushed further left
            start = i

            # check if the bar at the top of the stack is
            # taller than the current bar h.
            # b/c the current bar is shorter, the taller bar
            # cannot extend any further right than index i-1,
            # its right boundary is confirmed.
            while stack and stack[-1][1] > h:
                # removes that taller bar from the stack to
                # resolve its maximum possible rectangle.
                index, height = stack.pop()
                
                # compute the popped bar's area.
                maxArea = max(maxArea, height * (i - index))

                # since the popped bar had height > h, the
                # current shorter bar h can span backwards 
                # and take over that popped bar's starting
                # position so we shift start back to index.
                start = index

            # pushes the current height h parid with its
            # earliest possible start index onto the stack.
            # at this point, the heights in the stack remain
            # strictly increasing.
            stack.append((start, h))

        # after iterating thru the entire histogram, any elements
        # left in the stack never encountered a bar shorter than
        # themselves to the right, that means they can extend 
        # all the way to the end of the array.
        for i, h in stack:
            # the width for each remaining bar is len(heights) - i 
            # from its earliest start index i thru the end of hist
            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea