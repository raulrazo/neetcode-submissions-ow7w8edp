class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = 0
        maxCount = 0
        countMap = {}

        for i in range(len(nums)):
            countMap[nums[i]] = 1 + countMap.get(nums[i], 0)

            if countMap[nums[i]] > maxCount:
                majority = nums[i]
                maxCount = countMap[nums[i]]

        return majority