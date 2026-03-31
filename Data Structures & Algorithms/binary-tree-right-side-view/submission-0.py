# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        # initialize queue with root
        q = collections.deque([root])

        # while q is not empty
        while q: 
            rightSide = None
            # for this level, we are going to get the length
            qLen = len(q)

            # go thru every element at this level:
            for i in range(qLen):
                # go thru every element and pop it
                node = q.popleft()

                # node could be null so
                if node:
                    # update our rightSide to that node
                    rightSide = node

                    # so this means that after this loop is done executing
                    # rightSide will have the last node (rightmost) at 
                    # the end of the queue for this level

                    # take the current node's children and append them to our queue
                    q.append(node.left)
                    q.append(node.right)

            # after this for loop,
            # we popped every node at that level
            # and took their children and added them to the queue
            # AKA removed elements from the previous level and added the ones from the next level

            # right side could be null
            if rightSide:
                res.append(rightSide.val)

        return res




        