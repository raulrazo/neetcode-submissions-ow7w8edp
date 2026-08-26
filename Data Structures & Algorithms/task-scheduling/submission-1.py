class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)

        maxHeap = [-cnt for cnt in count.values()]

        heapq.heapify(maxHeap)

        time = 0

        q = deque()

        while maxHeap or q:
            time += 1

            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)

                if cnt:
                    q.append([cnt, time + n])

            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time

        # O(n) time complexity because we have to process all of the tasks
        # O(1) space complexity because we are storing alphabet char and at most there are 26 different letters.

            
        