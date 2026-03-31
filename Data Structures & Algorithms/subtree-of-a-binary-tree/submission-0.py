# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # base case: t is empty = will be subtree regardless of s 
        if not subRoot: return True
            
        # base case: s is empty but t is non-empty = t cannot be a subtree of s = false
        if not root: return False

        # now we know both trees are non-empty so we compare them using sameTree
        # if both of the trees are the same then we can return True
        if self.sameTree(root, subRoot): 
            return True

        # if they are not the same tree, we can still compare t with left and right subtree of s using recursion AKA isSubtree function
        
        # if either of these return true then we can return true because we only want to know if t is a subtree in at least one of the trees in s
        return (self.isSubtree(root.left, subRoot) or
            self.isSubtree(root.right, subRoot))

    def sameTree(self, s, t):
        # first base case: if we are given empty trees
        if not s and not t:
            # both empty = same tree technically so return true
            return True

        # make sure both are not empty 
        # if s and t are non-empty and the values of both of them are the same
        if s and t and s.val == t.val:
            # we still have to compare the left and right subtrees of nodes s and t and check if they're the same
            # so recursive shit, if they are the same then this will return True 
            return(self.sameTree(s.left, t.left) and 
                self.sameTree(s.right, t.right))

        # third case: at least one tree empty and one tree non empty
        # so we return False because they are not the same
        return False


        