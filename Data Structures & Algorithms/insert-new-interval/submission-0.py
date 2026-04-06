class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # result of intervals
        res = []

        for i in range(len(intervals)):
            # edge cases
            # if new interval goes before curr interval
            # AKA end value of new is less than start of curr
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                # we know the remaining intervals won't overlap so return now
                return res + intervals[i:]

            # if new interval goes after curr interval
            # it could still be overlapping with intervals to the right
            # so we don't append right away
            # AKA start value of new is greater than end of curr
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])

            # means new interval is overlapping
            else:
                # merge new with curr interval 
                # take minimum of the starting value of both intervals
                # take maximum of ending value of both intervals
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
                # we don't add this new interval yet because it could still be overlapping
                # with other intervals we haven't seen yet

        # there are two ways we could have exited this for loop
        # if the exit in the for loop never happened
        # then we are never going to end up adding the new interval to the result
        # so let's add it
        res.append(newInterval)

        return res
            
        