class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # converts the problem from finding the k-th largest
        # element to finding the element at the (n - k) index
        # in a sorted array because we are going to sort this.
        k = len(nums) - k

        def quickSelect(l, r):
            # selects the rightmost element as the pivot value
            # around which to partition.
            pivot = nums[r]

            # sets the partition boundary potiner p to l.
            # every element place before index p will be smaller 
            # or equal to the pivot.
            p = l

            # scans each element in the subarray, excluding the 
            # pivot at r.
            for i in range(l, r):
                # checks if the current element belongs on the
                # left side of the partition.
                if nums[i] <= pivot:
                    # swaps nums[i] into index p, grouping 
                    # elements less than or equal to the 
                    # pivot to the left.
                    nums[p], nums[i] = nums[i], nums[p]

                    # advances the boundary pointer p to reserve
                    # space for the next element smaller than or
                    # equal to the pivot.
                    p += 1

            # swaps the pivot element from index r into index p.
            # the pivot is now fixed at index p in its final
            # sorted position: all values to its left are <=
            # pivot and all values to its right are > pivot
            # DNU: How do we know all values to its right are >?
            nums[p], nums[r] = nums[r], nums[p]

            # the target index k lies in the left partition
            # so recursively search subarray to the left
            if p > k:
                return quickSelect(l, p - 1)

            # the target index k lies in the right partition
            # so recursively search subarray to the left
            elif p < k:
                return quickSelect(p + 1, r)

            # this means the pivot is at the exact right index
            else:
                return nums[p]

        return quickSelect(0, len(nums) - 1)


        