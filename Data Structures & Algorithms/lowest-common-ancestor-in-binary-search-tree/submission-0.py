# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # start at the root node and continue until we find our result
        cur = root

        # it is never going to be null because we are guaranteed to find a result
        # but this is way to execute forever until we find that result
        while cur:
            # p val and q val are greater than the root we are visiting then we have to go down the right subtree because BST properties
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right 
            # p val and q val are less than the root we are visiting then we have to go down the left subtree because BST properties
            if p.val < cur.val and q.val < cur.val:
                cur = cur.left 
            # if our split occurs or we end up finding p or q, which means we have found our result which is current itself
            else:
                return cur 
        