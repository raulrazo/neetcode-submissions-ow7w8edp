class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # acts as the write pointer.
        # the element at index 0 is inherently unique so
        # it is already in its correct position
        # so the next unique element must be at position 1 
        # so we set l to 1.
        l = 1

        # start from 1 because of prior explanation
        # iterate through nums
        # r acts the read pointer
        for r in range(1, len(nums)):
            # in arrays increasing in sorted order, duplicates
            # are always next to each other so if this num
            # is different from the one before it, then we know
            # a unique value has appeared.
            if nums[r] != nums[r - 1]:
                # overwrites the value at the write position l
                # with the newly discovered unique values nums[r].
                nums[l] = nums[r]

                # increments l by 1 to reserve the next slot for
                # the subsequent unique element.
                l += 1

        # b/c l was incremented every time a unique element was
        # placed, its final value equals the exact count of unique
        # elements (k) so we can return it
        return l

        # Time and Space Complexity

        # O(n) time complexity where n is the length of nums
        # b/c we perform a single linear pass through nums.

        # O(1) space complexity because we did not use any
        # extra space.
