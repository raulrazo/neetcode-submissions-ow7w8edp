class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # preallocates res with 1s b/c
        # 1s give us a good base for multiplication.
        res = [1] * (len(nums))

        # tracks the running cumulative product of
        # all elements left to curr index i.
        prefix = 1

        # scans left to right
        for i in range(len(nums)):
            # assigns the accumlated product (prefix)
            # of all elements before this i into res[i]
            res[i] = prefix

            # so subsequent indices receive the updated 
            # product.
            prefix *= nums[i]

        # tracks the running cumulative product of
        # all elements right to curr index i.
        postfix = 1
        
        # scans right to left
        for i in range(len(nums) - 1, -1, -1):
            # multiplies the exisiting prefix at res[i]
            # by the postfix, and the result is the 
            # total product of all elements execept
            # nums[i].
            res[i] *= postfix

            postfix *= nums[i]

        return res 
        