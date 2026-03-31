class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # initially a minHeap is just an array in Python
        minHeap = []
        
        # go through every pair of points and compute the distance
        for x,y in points:
            dist = (x ** 2) + (y ** 2) # x squared and y squared
            minHeap.append([dist, x, y]) # distance is going to go first because that is the key value for our minHeap

        # now we can turn our list into a heap
        heapq.heapify(minHeap) # this will reorder the list to make sure that it is in the structure of a heap

        res = []

        while k > 0: # keep popping from our minHeap
            dist, x, y = heapq.heappop(minHeap)

            res.append([x, y])

            k -= 1

        return res



        