class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in values:
                res = [values[diff], i]

            values[nums[i]] = i

        return res
        