class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        product = 1

        res = 0

        l = 0

        for r in range(len(nums)):
            print(f"Iteration: {r}")
            product *= nums[r]
            print(f"Calculated product: {product}")

            while l <= r and product >= k:
                product = product // nums[l]
                print(f"Shrunken Product: {product}")
                l += 1

            res += (r - l + 1)

        return res
        