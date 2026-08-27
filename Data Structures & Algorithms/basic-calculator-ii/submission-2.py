class Solution:
    def calculate(self, s: str) -> int:
        # initialize empty stack
        stack = []
        
        # initialize starting num
        num = 0

        # initialize starting op
        op = '+'

        s = s.replace(' ', '')

        for i, ch in enumerate(s):
            if ch.isdigit():
                num = (num * 10) + int(ch)

            if (not ch.isdigit()) or i == len(s) - 1:
                # apply our previous op
                if op == "+":
                    stack.append(num)

                elif op == "-":
                    stack.append(-num)

                elif op == "*":
                    stack.append(stack.pop() * num)

                else:
                    stack.append(int(stack.pop() / num))

                op = ch
                num = 0

        return sum(stack)
        