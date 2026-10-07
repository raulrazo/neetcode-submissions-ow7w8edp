class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]

        curSum = 0

        for num in nums:
            # if the running sum becomes negative, keeping it
            # will only reduce the sum of any futrue subarray.
            if curSum < 0:
                # so we reset it
                curSum = 0

            curSum += num
            maxSub = max(maxSub, curSum)

        return maxSub
        