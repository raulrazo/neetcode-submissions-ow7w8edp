# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        q = collections.deque()
        q.append(root) # initialize the q with the root

        while q: # while our q is not empty
            qLen = len(q) # get the number of nodes or value that are in this queue currently

            # loop through every single one of those values AKA one level at a time
            level = []

            for i in range(qLen):
                node = q.popleft()
                # if node is not null
                if node:
                    level.append(node.val)
                    # make sure to add the children of this node since we popped it
                    q.append(node.left)
                    q.append(node.right)

                    # could be null but that is why we have this if statement

            if level: # make sure level is not empty or has null nodes
                res.append(level)

        return res


        