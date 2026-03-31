class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        prevMap = set()

        for num in nums:
            if num in prevMap:
                return True

            prevMap.add(num)

        return False