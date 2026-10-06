class Solution:
    def isHappy(self, n: int) -> bool:
        # tracks every number produced during the transformation
        # sequence to detect repetitions.
        visit = set()

        # checks whether the current value already exists in 
        # visit.
        # if n is found in visit, a cycle has formed, causing the 
        # loop to terminate immediately. 
        while n not in visit:
            # insert the current n into the visit set before
            # transforming it.
            visit.add(n)

            # update n
            n = self.sumOfSquares(n)

            # base success condition
            if n == 1:
                return True

        # reached only when while n not in visit is False
        return False
    
    # helper function
    def sumOfSquares(self, n: int) -> int:
        # holds the running total of squared digits
        output = 0

        # continues extracting digits until all digits of n
        # have been processed and n becomes 0.
        while n > 0:
            # extract the rightmost digit in n
            digit = n % 10 # 145 % 10 = 5

            # squares the extracted digit and adds it to output
            digit = digit ** 2
            output += digit

            # cuts off the right most digit
            n = n // 10 # 145 // 10 = 14

        # return the calculated sum of the squared digits
        return output


        # Time and Space Complexity

        # O(log n) time complexity b/c somehow with math, 
        # extracting and squaring each digit takes that time.

        # O(log n) space complexity b/c every time we extract and
        # square we add to the set and we do that log n times so
        # set will log n size. 
