class Solution:
    def reverseBits(self, n: int) -> int:
        # declare result variable
        res = 0
        # imagine this is 32 bits of 0

        # go thru every single bit in the input
        for i in range(32):
            # the first thing we want to do is get the ith bit of n
            # we do that by taking n and shifting it to the right by i
            # and this makes our target bit go in the 1s spot 
            # so we can just take it and & it with 1 and get the result bit we are looking for
            bit = (n >> i) & 1
            
            # put that bit in our result
            # start at the largest bit and work our way down
            # shift our bit to the left by 31 - i
            # and that is how we shift the 1 that we OR with
            res = res | (bit << (31- i)) 

        return res
        