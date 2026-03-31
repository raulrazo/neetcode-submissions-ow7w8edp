# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # the base case: if the first tree is empty and the second tree is empty
        if not p and not q:
            # return True b/c they are both empty trees and empty trees are technically equal
            return True

        # if only one of them are empty
        if not p or not q:
            # they are not the same tree so we return false
            return False

        # if neither of the above statement executes that means both of the trees are non-empty and now we can look at the values
        if p.val != q.val:
            # means the values are not the same so the trees are not the same -> false
            return False

        # if these statement did not execute that means both p and q are non-empty and their values are the same -> good
        # now we do the recursive step 
        # we want both of these functions calls to return tree because that means subtrees are the same
        # so we and them together and return the result
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
        