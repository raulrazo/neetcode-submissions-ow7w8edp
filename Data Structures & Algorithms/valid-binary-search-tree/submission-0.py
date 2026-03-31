# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # helper function 
        # pass in node because recursion, and left and right boundaries
        def valid(node, left, right):
            # base case: reach a null node
            if not node:
                return True

            # do the boundary checking / comparison
            if not (node.val < right and node.val > left):
                # this node breaks the boundaries so return false
                return False

            # recursive call
            # make sure the left subtree of node is valid
            # since we are going left we leave left boundary the same
            # update right boundary to node's value because every value in the left subtree has to be less than the parent, so the parent becomes the right boundary 

            # and make sure that the right subtree is valid
            # same logic as left
            
            # whatever this evaluates to is going to be our result (?)
            return (valid(node.left, left, node.val) and
            valid(node.right, node.val, right))

        # call recursive function
        return valid(root, float("-inf"), float("inf")) 
        