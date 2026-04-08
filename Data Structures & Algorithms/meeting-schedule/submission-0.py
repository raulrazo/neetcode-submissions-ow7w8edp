"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # sort the intervals based on start time
        # i = interval
        # sorting it by i of start AKA start time of that interval
        intervals.sort(key = lambda i : i.start)

        # iterate thru all intervals
        # start at index 1 so we can compare two intervals off the bat
        for i in range(1, len(intervals)):
            i1 = intervals[i - 1] # first interval
            i2 = intervals[i]

            # compare end time of i1 and start time of i2
            # if and only if the start time of i2 is less than the end time of i1
            # that means they are overlapping so return false
            if i1.end > i2.start:
                return False

        
        # never overlapped so return true
        return True
