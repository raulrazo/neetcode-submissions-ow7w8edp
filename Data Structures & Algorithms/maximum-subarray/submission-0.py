class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # initialize our max subarray with the default first value of the nums array because
        # it has to be something and it can't be 0 because we know we have negative values in this array?
        maxSub = nums[0]

        # going to be constantly computing our current sum so initialize that to 0
        curSum = 0

        # go thru each number in nums
        for n in nums:
            # if we had a negative prefix, then we remove that portion from the current sum
            # and the way we can check this is to check if current sum is at any point negative
            if curSum < 0:
                # we remove that portion by just setting current sum back to 0
                curSum = 0

            # after that, we can add our current number to the current sum
            # this will make sure that we are always computing the maximum that we can
            curSum += n

            # this current sum could be the max so we have to update our max subarray
            maxSub = max(maxSub, curSum)

        # return that bitch
        return maxSub
        