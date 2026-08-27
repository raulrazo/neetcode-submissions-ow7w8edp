class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # runs binary search with leftbias = true 
        # to locate the first (leftmost) occurence
        # of the target.
        left = self.binarySearch(nums, target, True)

        # runs binary search with leftbias = false 
        # to locate the last (rightmost) occurence
        # of the target.
        right = self.binarySearch(nums, target, False)

        # if target is not in nums then both calls
        # return -1.
        return [left, right]

    def binarySearch(self, nums, target, leftBias):
        # initialize binary search two pointer boundaries
        l = 0
        r = len(nums) - 1

        # initializes answer placeholder to -1
        # and if target is never encountered in the loop
        # then this is how we return -1.
        i = -1

        # executes the search loop as long as the 
        # search window is valid.
        while l <= r:
            m = (l + r) // 2

            # if target > middle then it must be
            # in the right half of the list
            # so discard the left half and mid pointer
            # by shifting l to m + 1.
            if target > nums[m]:
                l = m + 1

            # if target < middle then it must
            # reside in the left half so same as before
            elif target < nums[m]:
                r = m - 1

            # target = middle so match is found
            else:

                # update i to the middle index
                # b/c this is now a valid candidate
                # for the result.
                i = m

                # if we're searching for leftmost
                if leftBias:
                    # shift the right boundary to
                    # m - 1 to force next search step
                    # into the left subarray to check if
                    # an even earlier occurence exists
                    r = m - 1
                else:
                    # same concept as before but checks
                    # if an even later occurence exists
                    l = m + 1

        # returns the most recently recorded index
        return i
        