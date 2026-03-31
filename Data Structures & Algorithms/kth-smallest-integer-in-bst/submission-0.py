# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # will tell us the number of elements we visited in our tree
        n = 0

        stack = []
        cur = root # tells us the node we are currently at

        while cur or stack: # while cur is not null and stack isn't empty
            while cur: # while cur is not null, we want to keep going left
                stack.append(cur)
                cur = cur.left

            # when that loop is done executing that means curr is at null
            # and we have reached the end of left

            cur = stack.pop()
            # when we pop it, we process it
            n += 1
            if n == k: # that means the current node we just processed is the value we are looking for
                return cur.val
            
            # then we check the right and repeat the process
            cur = cur.right


        