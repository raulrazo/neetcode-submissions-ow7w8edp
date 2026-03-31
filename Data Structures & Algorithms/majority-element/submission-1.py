class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        maxCount = 0
        majority = 0

        # key = number : value = occurences

        for i in range(len(nums)):
            hashmap[nums[i]] = 1 + hashmap.get(nums[i], 0)
            if hashmap[nums[i]] > maxCount:
                majority = nums[i]
                maxCount = hashmap[nums[i]]


        return majority 