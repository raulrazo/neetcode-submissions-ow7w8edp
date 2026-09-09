"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # extracts all start timestamps into an array and sorts them
        start = sorted([i.start for i in intervals])

        # extracts all end timestamps into an array and sorts them
        end = sorted([i.end for i in intervals])

        # tracks the peak of count observed so far
        res = 0

        # tracks the number of rooms currenly occupied at the active
        # point in time.
        count = 0

        s, e = 0, 0

        # continues until all meetings have started.
        # once s == len(intervals), no additional rooms will ever be
        # needed and remaining meetings while only finish and decrement
        # count. 
        while s < len(intervals):
            # evaluates whether the next chronological event is
            # a meeting start.
            # because start[s] < end[e], a meeting must begin 
            # before the earliest pending meeting wraps up.
            if start[s] < end[e]:
                # advances the start pointer to the next scheduled time
                s += 1

                # allocates an additional room
                count += 1

            else:
                # advances to the next earliest ending meeting
                e += 1

                # frees up a room
                count -= 1

            res = max(res, count)

        return res
        