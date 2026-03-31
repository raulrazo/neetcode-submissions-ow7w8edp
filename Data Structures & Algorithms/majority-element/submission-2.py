class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        # key = num : value = occurences
        majority = 0
        maxCount = 0

        for i in range(len(nums)):
            count[nums[i]] = 1 + count.get(nums[i], 0)
            if count[nums[i]] > maxCount:
                majority = nums[i]
                maxCount = count[nums[i]]

        return majority