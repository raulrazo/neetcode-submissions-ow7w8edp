class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0

        # continue counting 1s while n is not equal to 0
        while n:
            # n % 2 will either be a 1 or 0
            res += n % 2

            # shift everything to the right by 1
            n = n >> 1

        return res
        