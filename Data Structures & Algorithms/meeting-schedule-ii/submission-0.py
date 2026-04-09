"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # create our start and end arrays in sorted order
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        # result is max count
        # count is number of meetings happening at any given time
        res, count = 0, 0

        # pointers for start and end array
        s, e, = 0, 0

        # we choose s because we know s will reach end of intervals
        # before e does because the start times are always before the end times
        while s < len(intervals):
            if start[s] < end[e]:
                # we have one additional meeting going on rn
                s += 1
                count += 1
            else:
                e += 1
                count -= 1

            res = max(res, count)

        return res


        