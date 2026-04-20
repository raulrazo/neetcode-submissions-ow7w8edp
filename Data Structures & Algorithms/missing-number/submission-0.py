class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # set it to len(nums) because we want to add the final value
        res = len(nums)

        for i in range(len(nums)):
            # this is doing the two sum thing in place
            # this is adding every value from the actual range but subtracting every value from nums
            res += (i - nums[i])
        
        return res