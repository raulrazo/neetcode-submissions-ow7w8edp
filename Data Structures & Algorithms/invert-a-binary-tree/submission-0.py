# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # check the base case
        if not root: # if the root is not null
            # then we can return null
            return None

        # swap the children
        tmp = root.left # save the left value in a temp variable
        root.left = root.right # replace the root.left value with root.right
        root.right = tmp # replace the root.right value with the left value which we know is now stored in temp
        # AKA swapping the nodes

        # after swapping the nodes, we recursively invert the subtrees
        self.invertTree(root.left) # invert left subtree
        self.invertTree(root.right) # invert right subtree

        return root
        