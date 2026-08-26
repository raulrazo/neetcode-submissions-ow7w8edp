class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        res = 0

        l = 0

        product = 1

        for r in range(len(nums)):
            product *= nums[r]

            while l <= r and product >= k:
                product = product // nums[l]

                l += 1

            # DNU: Why do we add the entire size of window everytime?

            res += (r - l + 1)

        return res
        