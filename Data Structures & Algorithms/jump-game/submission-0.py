class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # define our goal as the end
        goal = len(nums) - 1

        # go backwards thru nums
        # start at last index, traverse to the beginning, up until we reach the 0th index
        for i in range(len(nums) - 1, -1, -1):
            # can this maximum jump starting at position i
            # greater than or equal to the goal
            # b/c if it is then that mean's we can reach the goal
            if i + nums[i] >= goal:
                # shift our goal post
                # i is the position that we are jumping from
                goal = i

        # when we reach the end
        # goal will be 0 meaning from the starting position we can reach the goal
        # if goal is greater than 0 then it means we can't
        return True if goal == 0 else False
        