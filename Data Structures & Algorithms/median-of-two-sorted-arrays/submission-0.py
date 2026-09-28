class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # initialization and ensuring A is the smaller array.

        A = nums1
        B = nums2

        # computes the combined count of all elements across
        # both arrays.
        total = len(nums1) + len(nums2)

        # calculates how many total elements must be on the
        # left side of our combined partition (???).
        half = total // 2

        # ensure A is alwasy the shorter or equal length array.
        if len(B) < len(A):
            A, B = B, A

        # search range and index calculation.
        l = 0
        r = len(A) - 1

        # a valid partition is mathematically guaranteed to exist
        # b/w the two sorted arrays, so this loop will always
        # terminate via a return statement.
        while True:
            # rightmost index from A that is in left partition
            i = (l + r) // 2

            # rightmost index from A that is in left partition
            j = half - i - 2

            # boundary elements and edge handling

            # the largest element from A in left partition.
            # if i < 0, no elements from A are in the left
            # partition so we default to -infinity.
            Aleft = A[i] if i >= 0 else float("-infinity")

            # smallest element from A in right partition
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")

            # largest element from B in the left partition
            Bleft = B[j] if j >= 0 else float("-infinity")

            # smallest element from B in the right partition
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")


            # paritition validation and median calculation.
            
            # checks if every element in the left partition is
            # less than or equal to every element in the right
            # partition.
            if Aleft <= Bright and Bleft <= Aright:
                # if the combined length is odd, the left
                # partition has total // 2 elements, meaning
                # the median is the very first element of 
                # the right partition.
                if total % 2:
                    return min(Aright, Bright)

                # if combined length is even, the median is
                # the average b/w largest element on left
                # and smallest element on right
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2

            # if Aleft is too large to belong in the left
            # parition, move the binary search cut in A to 
            # the left.
            elif Aleft > Bright:
                r = i - 1

            # Bleft > Aright meaning A contributed too few
            # elements to the left partition, move the cut
            # in A to the right
            else:
                l = i + 1
