class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # create our dp cache
        # initially every value is going to be set to 1
        LIS = [1] * len(nums)

        # iterate thru every index in the range of our input array
        # and do it in reverse order
        # len(nums) - 1 = start at last index
        # -1 = going backward
        # - 1 = going all the way to index 0
        for i in range(len(nums) - 1, -1, -1):
            # nested loop because we want to iterate thru
            # every subsequence that came after i
            # starting at i + 1 then going to end of input array
            for j in range(i + 1, len(nums)):
                # is value at i less than value at j 
                # b/c we want to this to be increasing
                if nums[i] < nums[j]:
                    # then we can update LIS at i
                    # LIS[i] = 1 b/c of default value
                    LIS[i] = max(LIS[i], 1 + LIS[j])

        # return the max of our list
        return max(LIS)


        