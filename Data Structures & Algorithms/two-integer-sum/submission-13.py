class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}

        for i, n in enumerate(nums):
            diff = target - n

            if diff in values:
                return [values[diff], i]

            values[n] = i

            
        