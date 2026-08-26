class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # DNU: how do lambda functions work, how does code know what we mean by the word 'pair'
        # sort the intervals by their start time
        # which is index 0
        intervals.sort(key=lambda pair: pair[0])

        # intialize the output list with first interval
        output = [intervals[0]]

        # for each start and end time 
        # for an interval in the intervals list
        for start, end in intervals:
            # get the end time of the last / most recent interval
            # in our output list
            lastEnd = output[-1][1]

            # if the start time for this current interval
            # is less than the end time for our last interval
            if start <= lastEnd:
                # then the current interval starts before our last one
                # so they overlap and we merge them
                # by taking the biggest (or farthest) end time
                # between this current interval and our last interval
                # -1 is for the last index of output list
                # [1] is for the 2nd index of that pair
                # for that interval which is the end time
                output[-1][1] = max(lastEnd, end)
            # if the start time for this current interval
            # is greater than the end for our last interval
            else:
                # the current interval starts after our last one ends
                # and they do not overlap and we don't need to merge
                # so we can just add it to the end of our output list
                # and it becomes our new last / most recent interval
                output.append([start, end])

        # return the output list we built with the for loop
        return output

        # O(n logn) time complexity because of sorting algorithm 
        # O(n) space complexity because the memory of the output list

        