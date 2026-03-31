class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # set res to max to get the highest number just in case
        # nums[0] is - 1 or something
        res = max(nums)

        # set min and max to neutral values
        curMin, curMax = 1, 1

        for n in nums:

            # temp variable so our curMin doesn't tweak out when we put cur max in it
            tmp = curMax * n

            # cur max could be the new number that we just found multiple by the cur max if the cur max is positive and n is positive
            # cur max could also be n multiplied by the cur min because n could be negative and cur min could be negative and that can be a positive number
            # third option is n itself because n could be multiplied by -1 and that would ruin it but this could just take n itself which is greater than n * -1
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(tmp, n * curMin, n)

            # update our result with max product
            res = max(res, curMax)
        return res
        