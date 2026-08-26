class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # initialize result
        res = 0

        # initialize left pointer for sliding window
        l = 0

        # set initial sliding window product to 1
        # b/c 1 is a neutral value and we don't want to multiply by 0
        product = 1

        # going to use our right pointer as the thing in the for loop
        for r in range(len(nums)):
            # update our product everytime we see a new number
            # multiply by new number at the right pointer
            product *= nums[r]

            # for every valid subarray,
            # we want to update the result and add to it
            # the size of that subarray
            # but we can only do so if it's valid
            # so let's make sure it's valid
            # AKA the product is not greater than or equal to k
            # and we gotta check that left pointer does not pass right pointer
            while l <= r and product >= k:
                # get the value at the left pointer
                # and update our current product since we are shrinking the window
                # and we do that thru that division concept
                product = product // nums[l]

                # update the product / shrink the window
                l += 1

            # update our result with number of subarrays
            # which is size of the current window
            res += (r - l + 1)

        return res


        