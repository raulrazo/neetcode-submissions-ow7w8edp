# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # take care of the base case first
        # if the root is null
        if not root:
            return 0

        # return 1 + the max depth of the left subtree and the right subtree
        # taking the result of both function calls and figuring out what's the max subtree's depth of both of the subtrees
        # and adding 1 to it because the current root node is definitely not null
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        