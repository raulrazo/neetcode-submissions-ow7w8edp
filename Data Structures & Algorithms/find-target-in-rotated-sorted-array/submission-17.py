class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if target == nums[mid]:
                return mid

            # checks if the left half, l to mid
            # is strictly sorted. 
            if nums[l] <= nums[mid]:
                # evaluates whether target falls outside the sorted left range.

                # target > nums[mid]: target is strictly than the highest value
                # in this sorted half.

                # target < nums[l]: target is strictly smaller
                # than the smallest value in this 
                # sorted half. 
                if target > nums[mid] or target < nums[l]:
                    # if either is true, target cannot
                    # exist between l and mid so we 
                    # discard the left half by setting 
                    # l = mid + 1.
                    l = mid + 1
                else:
                    # if target is within l to mid then
                    # the right half is discarded.
                    r = mid - 1

            else:
                # If nums[l] > nums[mid], the 
                # pivot exists in the left 
                # half, which guarantees the 
                # right half nums[mid...r] is 
                # strictly sorted.

                # Evaluates whether target 
                # falls outside the sorted 
                # right range:

                # target < nums[mid]: Target 
                # is smaller than the lowest 
                # value in this sorted half.

                # target > nums[r]: Target is 
                # larger than the highest 
                # value in this sorted half.
                if target < nums[mid] or target > nums[r]:
                    # if either is true, 
                    # target cannot exist 
                    # between mid and r. We 
                    # discard the right half 
                    # by setting r = mid - 1.
                    r = mid - 1
                else:
                    # Target lies within 
                    # (nums[mid], nums[r]], 
                    # so the left half is 
                    # discarded.
                    l = mid + 1

        return -1

        