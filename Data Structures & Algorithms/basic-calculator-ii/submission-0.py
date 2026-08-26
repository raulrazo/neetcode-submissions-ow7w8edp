class Solution:
    def calculate(self, s: str) -> int:
        # initialize empty stack
        stack = []

        # initialize "empty" num
        num = 0

        # initalize "previous" op
        op = '+'

        # remove all spaces from the string 
        s = s.replace(' ', '')

        # for position and char in number string
        for i, ch in enumerate(s):
            # if it's a digit
            if ch.isdigit():
                # build up our current num
                # by multipling it by 10 and giving it a zero at the end
                num = num * 10 + int(ch)

            # if not a digit and not the last schpot, 
            # then it must be an operator,
            # check which
            if (not ch.isdigit()) or i == len(s) - 1:
                # if it's a plus, 
                # we push current num to top of stack
                if op == '+':
                    stack.append(num)

                # if it's a minus
                # we push the negative of the curr num to stack
                # b/c when we add all of them together,
                # the negative will account for the minus
                elif op == '-':
                    stack.append(-num)
                
                # if it's a multiplication
                # we still push the curr num to stack,
                # but we multiply with the current top of stack before
                # b/c mult and divide are priority in PEMDAS
                # so we must do them right away
                # and we do it with the top of our stack
                # b/c that must be the most recent number
                # that we've seen in the string
                # and that we need to do this op with
                elif op == '*':
                    stack.append(stack.pop() * num)

                # or we get division
                # and it's the same concept as mult
                else:
                    # DNU: Does calling stack.pop() actually pop the stack?
                    stack.append(int(stack.pop() / num))

                # wait, what
                # DNU: Why do we reset everything?
                op = ch
                num = 0

        return sum(stack)

