class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort the list of intervals
        intervals.sort()

        # initialize result
        res = 0

        # keep track of first end val in our sorted interval
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            # are they overlapping
            # they are not overlapping if the start val
            # that we are looking at is >= to the previous end val
            if start >= prevEnd:
                # not overlapping so only thing we need to do
                # is update our prevEnd to new end val
                prevEnd = end
            # if they are overlapping
            else:
                # then we need to remove one of the intervals
                # so increment result count
                res += 1

                # to remove, we update our prevEnd
                # b/c we don't need to actual delete the interval in the array
                # we just need to count
                # new end will be the interval with minimum end val
                prevEnd = min(end, prevEnd)

        return res
        