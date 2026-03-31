class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # put all of the stones into a maxHeap
        # gotta use minHeap so multiply all the values in stones by -1
        # going thru every single stone and putting it into a list and multiplying each stone by negative 1
        stones = [-s for s in stones]
        
        # now we want to turn this list into a heap
        heapq.heapify(stones) # O(n) time operation

        while len(stones) > 1: # want to continue this while the number of stones is greater than 1
            # get two largest stones
            first = heapq.heappop(stones) # first largest
            second = heapq.heappop(stones) # second largest

            if second > first: # second stone could have smaller or equal weight to first, greater than because they are negative
                # take the difference b/w the two and add it back to the heap
                # substracting first - second because they are negative
                heapq.heappush(stones, first - second)  


        # edge case if stones is left empty
        # won't affect if stones is 1 because that 1 thing in stones will likely be bigger than 0
        stones.append(0)
        # return the positive value of whatever is left in stones
        return abs(stones[0])        