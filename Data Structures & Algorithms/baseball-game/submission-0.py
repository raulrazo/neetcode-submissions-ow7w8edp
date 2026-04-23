class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # initialize stack
        stack = []

        # iterate thru ops
        for op in operations:
            if op == "+":
                # get the top of the stack
                # -2 means 2nd to last one
                stack.append(stack[-1] + stack[-2])
            elif op == "D":
                # get the previous value (top of stack)
                stack.append(2 * stack[-1])
            elif op == "C":
                # invalidate last score that was added to stack
                stack.pop()
            else: 
                # its a number to convert to int and push to stack
                stack.append(int(op))

        # return the sum of all the scores
        return sum(stack)
