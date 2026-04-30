class MyQueue:

    def __init__(self):
        # declare two stacks
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        # just push to stack 1
        self.s1.append(x)

    def pop(self) -> int:
        # do not have to worry about edge case where queue is empty
        # b/c problem says pop() will only be called if queue is non-empty
        # same thing with peek()

        # if stack 2 is empty
        if not self.s2:
            # take everything from stack 1 and move it to stack 2
            while self.s1:
                self.s2.append(self.s1.pop())

        # ultimately we want to return from stack 2
        return self.s2.pop()

    def peek(self) -> int:
        # if stack 2 is empty
        if not self.s2:
            # take everything from stack 1 and move it to stack 2
            while self.s1:
                self.s2.append(self.s1.pop())

        # return the last element from stack 2
        return self.s2[-1]
        

    def empty(self) -> bool:
        # check that both stacks are empty
        return max(len(self.s1), len(self.s2)) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()