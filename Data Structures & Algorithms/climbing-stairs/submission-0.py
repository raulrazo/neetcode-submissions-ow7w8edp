class Solution:
    def climbStairs(self, n: int) -> int:
        # two variables for the two positions
        # that things depend on
        one, two = 1, 1

        # we are going to loop thru n - 1 times
        for i in range(n - 1):
            temp = one
            
            # update one
            # one + two b/c we are just adding the two previous values
            one = one + two

            # shift two to whatever the previous value of one was
            # that is the reason for the temp variable
            two = temp

        # cuz this will be the culmination of all the previous computed steps
        return one

        