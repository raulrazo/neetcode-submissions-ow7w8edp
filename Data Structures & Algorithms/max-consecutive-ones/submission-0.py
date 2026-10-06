class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # tracks the running streak of consecutive 1s
        cnt = 0

        # stores maximum consecutive 1s
        res = 0

        for num in nums:
            # if num is 1, streak continues, increment cnt.
            # if num is 0, streak breaks, reset cnt.
            cnt = cnt + 1 if num else 0

            # updates res
            res = max(res, cnt)

        return res

        # Time and Space Complexity

        # O(n) time complexity because we iterate thru all nums.

        # O(1) space complexity b/c we didn't use extra memory.