class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # each task 1 unit time
        # minimize idle time

        # count the occurences of each character in the input
        # use this built in way

        count = Counter(tasks)

        # create our maxHeap using those counts
        # iterate thru each count in the hashmap we just created
        # but we want to only iterate through the values
        # and we take negative of the count because in python we can only have minHeap
        # so negative values make it a maxHeap
        # so this is also just creating an array with every negative count that we computed

        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]

        # now we actually turn it into a heap
        # this takes the array and orders it in such a way that it is the max heap
        heapq.heapify(maxHeap)

        # var to keep track of what time it is
        time = 0

        # use double ended queue for queue
        q = deque() # pairs of [-cnt, idleTime]

        # while maxHeap is not empty or the q is not empty
        # as long as one of these is not empty, that means we have more tasks that we need to process
        while maxHeap or q:
            # increment time by 1
            time += 1

            # if maxHeap is non-empty, we pop from it
            if maxHeap:
                # get the count of the task we popped
                # also as we pop from the heap,
                # that means we are processing this task
                # so for some reason we add 1 to count
                # oh b/c we are using negative values,
                # if they were positive then we would subtract 1
                cnt = 1 + heapq.heappop(maxHeap)

                # if cnt is not zero
                if cnt:
                    # then we append the pair to our queue
                    # [count itself, time that it's going to be available again]
                    q.append([cnt, time + n])

            # if q is non-empty
            # and first val in our queue at index 1
            # which is the time
            # is equal to the current time
            # then that means we can pop it from our queue
            if q and q[0][1] == time:
                # get index of 0 b/c we care about the first value
                # which is the count 
                # we want to add that task (or value) back to our maxheap too tho
                heapq.heappush(maxHeap, q.popleft()[0])


        # return the time it took us to do all that work
        return time






        