class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0] # we can set this to any arbitrary default value
        l = 0
        r = len(nums) - 1

        # keep running our binary search while our pointers are in a valid position
        while l <= r:
            # if we ever get to a subarray that is already sorted
            if nums[l] < nums[r]:
                # then we can update our result potentially and break out of this
                res = min(res, nums[l])
                break        

            # if the array is not sorted that is when we are going to do binary search
            m = (l + r) // 2 # compute mid pointer: left + right integer division
            res = min(res, nums[m]) # potentially update result, why? because this while loop is the binary search

            # are we going to search to the left or to the right?
            if nums[m] >= nums[l]: # aka it is part of the left portion
                # so we want to search the right
                l = m + 1
            else: # we are in the right sorted portion
                # so we want to search the left
                r = m - 1

        return res


