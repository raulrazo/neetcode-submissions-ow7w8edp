class MyStack:

    def __init__(self):
        # initialize queue
        self.q = deque()

    def push(self, x: int) -> None:
        # just push it
        self.q.append(x)
        
    def pop(self) -> int:
        # loop until we reach the last value in our queue
        for i in range(len(self.q) - 1):
            # take our popped value and add it to the right side
            self.push(self.q.popleft())

        # last element is not added back to the queue
        # it is at the beginning now
        return self.q.popleft()
        

    def top(self) -> int:
        # return last value
        return self.q[-1]

    def empty(self) -> bool:
        # True if empty, false if not empty
        return len(self.q) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()