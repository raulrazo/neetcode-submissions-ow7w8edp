class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}
        # number : occurences
        majority = maxCount = 0

        for i in range(len(nums)):
            counts[nums[i]] = 1 + counts.get(nums[i], 0)
            if counts[nums[i]] > maxCount:
                maxCount = counts[nums[i]]
                majority = nums[i]

        return majority