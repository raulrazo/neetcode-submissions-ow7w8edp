class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # initialize result
        res = 0

        # initialize left pointer for current valid sliding window
        l = 0

        # set initial current sliding window product to 1
        # b/c 1 is a neutral value and we don't want to multiply by 0
        product = 1

        # going to use our right pointer as the thing in the for loop
        for r in range(len(nums)):
            # includes the current element nums[r]
            # into the active window's running product.
            product *= nums[r]

            # for every valid subarray,
            # we want to update the result and add to it
            # the size of that subarray
            # but we can only do so if it's valid
            # so let's make sure it's valid
            # AKA the product is not greater than or equal to k
            # and we gotta check that left pointer does not pass right pointer

            # if the product meets or exceeds k, the window
            # violates the constraint.
            # The loop shrinks the window from the left until
            # the product is strictly less than k (or until l
            # moves past r).
            while l <= r and product >= k:
                # get the value at the left pointer
                # and update our current product since we are shrinking the window
                # and we do that thru that division concept.
                # Removes nums[l] from the product by integer division
                product = product // nums[l]

                # shrink the window
                l += 1

            # update our result with number of subarrays
            # which is size of the current window.
            # Adds the number of valid subarrays ending
            # specifically at index r.

            # For a valid window [l, r], every contiguous
            # subarray ending at r whose start index ranges
            # from l to r is guaranteed to have a product < k.
            # There are exactly r - l + 1 such subarrays.

            # If no valid window exists (e.g., when nums[r] >=
            # k and l moves to r + 1), r - l + 1 evaluates to
            # 0, adding nothing.
            res += (r - l + 1)

        # Returns the accumulated count of all valid subarrays
        # across all right-end positions.
        return res


        