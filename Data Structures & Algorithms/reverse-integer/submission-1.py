class Solution:
    def reverse(self, x: int) -> int:
        # set overflow boundaries
        MIN = -2147483648  # -2^31,
        MAX = 2147483647  #  2^31 - 1

        # intialize result
        res = 0
        
        # while our original int x still has numbers
        while x:
            # get the last digit by modding x by 10
            digit = int(math.fmod(x, 10))

            # pop the last digit of x by dividing by 10
            x = int(x / 10)

            # these two ifs check for overflow
            # DNU: absolute no idea what this line does here
            if res > MAX // 10 or (res == MAX // 10 and digit > MAX % 10):
                return 0

            if res < MIN // 10 or (res == MIN // 10 and digit < MIN % 10):
                return 0

            # new digit will not cause overflow
            # so we add it to res, which is our current reversed digit
            # we add by multiplying res by 10 to add a 0 at the end of it
            res = (res * 10) + digit

        return res

        