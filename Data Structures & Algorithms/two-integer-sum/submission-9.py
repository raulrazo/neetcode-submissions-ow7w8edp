class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        # key = number : value = index

        for i, num in enumerate(nums):
            diff = target - nums[i]

            if diff in prevMap:
                return [prevMap[diff], i]

            prevMap[num] = i

        return 