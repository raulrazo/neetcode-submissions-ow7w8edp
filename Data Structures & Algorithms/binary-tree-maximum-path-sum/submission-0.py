# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # set result to value at root and make it a list because that'll make it so we can modify it within the recursive function

        res = [root.val]

        # resursive dfs, return max path sum without splitting
        def dfs(root):
            # base case: if the node is null
            if not root:
                # this mean we are not going to be adding anything
                return 0
            
            # get the max path sum

            # get the left max
            leftMax = dfs(root.left)

            # get the right max
            rightMax = dfs(root.right)

            # we got to this in case we get a negative value returned
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            # compute the max path sum WITH a split from this root node

            # add root.val with left max and right max because of split
            # this could potentially be our new result for some reason
            res[0] = max(root.val + leftMax + rightMax, res[0])

            # return value is going to be what we compute without splitting
            # choosing the largest sum
            return root.val + max(leftMax, rightMax)

        # this will update our res global variable
        dfs(root)

        return res[0]
        