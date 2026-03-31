class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # val : index
        prevMap = {}

        for i, n in enumerate(nums):
            diff = target - n

            if diff in prevMap:
                return [prevMap[diff], i]

            prevMap[n] = i
