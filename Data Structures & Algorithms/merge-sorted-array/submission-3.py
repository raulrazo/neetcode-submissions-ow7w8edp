class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # sets up the write pointer.
        # nums1 has a total capacity of m + n so index m + n - 1
        # points to very the last slot of nums1.
        # filling from the back guarantees we never overwrite 
        # unread elemetns in nums1.
        last = m + n - 1

        # continues iterating as long as both nums1 and nums2 have
        # unplaced elements.
        while m > 0 and n > 0:

            # compares the largest unprocessed element in nums1
            # with largest unprocessed element in nums2.

            # if the value in nums1 is greater, it belonds at
            # the current tail position, so we write it there
            # and decrement m to advance to the next largest
            # element in nums1.
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last] = nums1[m - 1]
                m -= 1
            else:
                # vice versa
                nums1[last] = nums2[n - 1]
                n -= 1

            # decrement destination index pointer by 1 to the
            # left to prepare for the next iteration. 
            last -= 1

        # handles leftover elements in nums2.
        # if the main loop exits with n > 0, it means all valid
        # elements originally in nums1 were larger and have
        # already shifted into their sorted positions at the end
        # so any remaining elements in nums2 must be placed into
        # the remaining front slots of nums1
        while n > 0:
            nums1[last] = nums2[n - 1]
            n -= 1
            last -= 1

        # Time and Space Complexity

        # O(m + n) time comeplexity because we have to iterate
        # thru both of the nums list.

        # O(1) space complexity because we do the merge in-place.


        