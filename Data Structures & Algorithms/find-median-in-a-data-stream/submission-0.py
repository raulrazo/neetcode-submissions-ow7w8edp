class MedianFinder:

    def __init__(self):
        # two heaps, large, small, minheap, maxheap
        # heaps should be equal size

        # in python, you can have a heap by just a list
        self.small, self.large = [], []
	
        

    def addNum(self, num: int) -> None:
        # always going to take num and add it to the small heap
        # python only does minheap so to get around that is we take every number and multiply it by -1
        heapq.heappush(self.small, -1 * num)

        # make sure every element in small is <= every element in large
        # if small and large are non null and the max value from small heap (multiply by -1 to get true value from the heap) is greater than the smallest value in our large heap
        if (self.small and self.large and (-1 * self.small[0]) > self.large[0]):
            # some value in our small heap is greater than our large heap
            # so we have to pop from our small heap and add to our large heap
            
            # get the largest value from our small heap
            val = -1 * heapq.heappop(self.small)
            
            # push that value to our large heap
            heapq.heappush(self.large, val)

        # the other condition we have to check is what if the size is uneven
        # meaning a differenc greater than 1
        if len(self.small) > len(self.large) + 1:
            # so we pop from the small and push to the large 
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # if large is bigger than small
        if len(self.large) > len(self.small) + 1:
            # pop from the large and push to the small
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        # if there is an odd length
        # AKA if the length of small is greater than the length of large 
        if len(self.small) > len(self.large):
            # return the largest value in small, which will be the one at the end 
            return -1 * self.small[0]
        
        # if the opposite is true
        if len(self.large) > len(self.small):
            # return the smallest value in large
            return self.large[0]

        # if neither of those are true that means we have an even number of elements
        # AKA heaps are the same size so we return the calculated median
        # AKA largest value in small heap + smallest value in large heap divided by 2
        return (-1 * self.small[0] + self.large[0]) / 2
        
        