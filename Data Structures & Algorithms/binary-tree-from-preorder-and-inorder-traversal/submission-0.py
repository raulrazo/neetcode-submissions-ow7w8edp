# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # base case: what if we don't have any node to traverse through the two arrays we are given?
        if not preorder or not inorder:
            # we don't have to create a tree
            return None

        # create root tree node with the first value of preorder array (always root)
        root = TreeNode(preorder[0])

        # whatever that value was, we want to find the position of it in the inorder array
        mid = inorder.index(preorder[0])

        # this is where we build the subtree

        # create left subtree recursively
        # we need to pass in the new preorder and inorder subarrays

        # for left subtree of preorder, mid tells us how many nodes we want in the left subtree
        # start at index 1 to skip root
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[ : mid])

        # create right subtree recursively
        # for preorder array, we need every value after the one we passed into the left function
        # for inorder, we want every node to the right of mid
        root.right = self.buildTree(preorder[ mid + 1 : ], inorder[ mid + 1 : ])

        # return the tree
        return root
        