class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # left boundary of sliding window
        l = 0

        # running sum of the elements within curr window
        total = 0

        # tracks the minimal valid window length found so far.
        # set to infinity so any valid subarray length found will
        # be strictly smaller.
        res = float("inf")

        # iterate the right pointer thru every index
        for r in range(len(nums)):
            # add the newly included element at index r to total
            total += nums[r]

            # enters a constraction loop as long as curr window
            # satisfies or exeeds the required sum.
            while total >= target:
                # updates res to the curr window length if shorter
                res = min(r - l + 1, res)

                # removes the element from the running sum before
                # shrinking.
                total -= nums[l]

                # shifts the left boundary one position to the
                # right, attempting to find a smaller subarray
                l += 1

        # if we never found a valid subarray then we return 0,
        # but if we did then we return res
        return 0 if res == float("inf") else res


        # Time and Space Complexity

        # O(n) time complexity because we iterate thru input.

        # O(1) space complexity b/c we didn't use extra memory.