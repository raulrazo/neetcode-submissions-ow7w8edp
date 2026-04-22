class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # go thru every value
        for i in range(len(nums)):
            # if the val at this index is negative
            # then change it to 0
            if nums[i] < 0:
                nums[i] = 0

        for i in range(len(nums)):
            # marking if a value exists in the input array
            # only doing it for vals that are in bounds
            val = abs(nums[i])
            if 1 <= val <= len(nums):
                # getting the index and make that val negative
                # if the val at that index is positive
                # b/c if it's negative already then we don't
                # need to be doing anything

                if nums[val - 1] > 0:
                    nums[val - 1] *= - 1
                elif nums[val - 1] == 0:
                    # edge case
                    nums[val - 1] = -1 * (len(nums) + 1)

        # now we find the solution
        # iterate thru solution set
        for i in range(1, len(nums) + 1):
            # if the val at computed index is >= 0
            # then i never showed up in the input array
            # and it is the first missing postive, AKA the answer
            if nums[i - 1] >= 0:
                return i

        # worst case answer
        return len(nums) + 1

        