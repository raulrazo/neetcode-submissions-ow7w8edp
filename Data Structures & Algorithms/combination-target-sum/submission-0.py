class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        # depth first search function
        def dfs(i, cur, total): # current is our combination
            # define base cases
            if total == target:
                res.append(cur.copy()) # create copy because we want to continue to use cur variable for recursion calls
                return
            
            # base cases if we end up being impossible to find a combination
            # if i is out of bounds, meaning we can't choose anymore candidates or our total ended up going over the target we are trying to reach
            if i >= len(nums) or total > target:
                return

            # recursive step
            # we can choose to include the value at candidates[i]

            # take that candidate and append it to our current combination
            # this is the decision where we include the candidate
            cur.append(nums[i])
            dfs(i, cur, total + nums[i])

            # this is the decision where we do not include the candidate
            cur.pop() # cuz we just added it for the other one
            dfs(i + 1, cur, total) # i + 1 indicating that we can't include any occurences of i

            # once this is done we have made our two decisions

        dfs(0, [], 0) # 0 as beginning index, empty array as beginning combination, 0 as our current total

        return res



        