# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        res = []

        def inorder(root):
            # base case if the root doesn't exist then we can just return
            if not root:
                return
            
            # inorder traversal
            inorder(root.left) # first we go through the left subtree
            
            # once the left is done then we have to process the root node itself
            res.append(root.val)

            inorder(root.right) # go through right subtree

        inorder(root)

        return res
        