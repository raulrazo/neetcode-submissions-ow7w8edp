# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        # create dfs helper function
        # b/c we need to pass in one more parameter that this outer function doesn't have
        def dfs(node, curSum):
            # base case 
            # if we ever have empty tree then we return false
            if not node:
                return False

            # if node is not null then we add it to curSum
            curSum += node.val

            # check if we found a path
            # so check if this node is a leaf node
            # so we check if it doesn't have any children
            if not node.left and not node.right:
                # if curSum = targetSum then this will return True
                # if not then this will return False
                return curSum == targetSum

            # if not a leaf node,
            # then we run DFS on the left and right side
            # but if one of these ends up returning true, then yay
            # so we make it a return statement
            return (dfs(node.left, curSum) or
                    dfs(node.right, curSum))


        # call our DFS function,
        # passing in the root
        # intialize curSum at 0
        return dfs(root, 0)

        