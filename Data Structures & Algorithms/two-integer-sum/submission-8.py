class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        # key = number , value = index

        for i, num in enumerate(nums):
            difference = target - nums[i]

            if difference in prevMap:
                return [prevMap[difference], i]

            prevMap[num] = i

        return

        