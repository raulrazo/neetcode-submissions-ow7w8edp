class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # intialize pointers for search window
        l = 0
        r = len(nums) - 1

        while l <= r:
            # calculate midpoint
            m = (l + r) // 2

            # m - 1 < 0 or nums[m - 1] != nums[m]: Validates 
            # whether the element to the left either does not 
            # exist (bounds check: m == 0) or is not equal 
            # to nums[m].

            # m + 1 == len(nums) or nums[m] != nums[m + 1]: 
            # Validates whether the element to the right either 
            # does not exist (bounds check: m == len(nums) - 1) or 
            # is not equal to nums[m].
            if ((m - 1 < 0 or nums[m - 1] != nums[m]) and
                (m + 1 == len(nums) or nums[m] != nums[m + 1])):

                # if nums[m] matches neighter neighbor, it has
                # no duplicate partner, therefore nums[m] is the 
                # unique target element
                return nums[m]

            # determines the count of elements strictly to the
            # left of the current pair.

            # If nums[m - 1] == nums[m], the pair consists of 
            # indices [m - 1, m]. All elements to the left of this 
            # pair span indices 0 through m - 2, totaling m - 1 
            # elements.

            # If nums[m] == nums[m + 1] (or if nums[m] pairs to 
            # the right), the pair starts at index m. The elements 
            # to the left span indices 0 through m - 1, totaling m 
            # elements.

            leftSize = m - 1 if nums[m - 1] == nums[m] else m

            # in an array where every item except one appears in
            # duplicate pairs, any subarracy containing only
            # matched pairs must have an even length. 

            # if leftSize is odd, the odd single element must
            # reside in the left partition.

            # if leftSize is even, the left partition is composed
            # entirely of intact pairs, the single element must
            # be in right side.

            if leftSize % 2:
                r = m - 1
            else:
                l = m + 1

        # Time and Space Complexity

        # O(log n) time complexity because of binary search and
        # cutting in half.

        # O(1) space complexity b/c we did not use any extra mem