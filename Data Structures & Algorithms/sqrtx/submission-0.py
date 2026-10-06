class Solution:
    def mySqrt(self, x: int) -> int:
        # sets the lower and upper bounds of binary search
        # range [0, x]. the sqrt of any non-negative interger x 
        # is guaranteed to lie within this interval.
        l = 0
        r = x

        # stores the largest interger m encountered so far where
        # m^2 <= x
        res = 0

        while l <= r:
            # calculate midpoint
            m = (l + r) // 2

            # checks whether m^2 overshoots x
            if m * m > x:
                # b/c the function f(n) = n^2 is non-decreasing
                # then any integer > m will also have a square 
                # greater than x so no point in checking them
                # so we discard right half.
                r = m - 1

            # checks if m^2 is smaller than x
            elif m * m < x:
                # since m^2 is less than x, a larger intger
                # might also satisfy the condiditon, so we
                # explore the right half with larger numbers
                l = m + 1

                # records m as the best candidate found so far
                res = m

            # exact square root found:
            else:
                # we found the result so just return m
                return m

        # return largest integer whose square was strictly
        # less than x.

        return res

        # Time and Space Complexity

        # O(log x) time complexity because we go from 0 to x
        # and binary search means log(n) because division by 2

        # O(1) space complexity because we use no extra memory

