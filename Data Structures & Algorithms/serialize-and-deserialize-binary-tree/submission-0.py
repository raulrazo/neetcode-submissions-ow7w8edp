# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # result string is going to be an array of characters first, then we join them all together with commas to make the final string
        res = []

        # preorder dfs
        def dfs(node):
            # base case: node is null
            if not node:
                # append the N character to result, N signifies null
                res.append("N")
                return	
            # if it is not null then we append that node value
            # convert it into a string tho
            res.append(str(node.val))

            # call recursive dfs on left and right subtree
            dfs(node.left)
            dfs(node.right)

        # once dfs is done executing our result string will be ready to return
        # but we gotta join them by commas first

        # call dfs
        dfs(root)

        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # we know that data is going to be command delimited so we are going to split it based on that comma
        vals = data.split(",")

        # we make i and self because we want it to be global
        self.i = 0

        # we don't need to pass anything into this because self.i is global
        def dfs():
            # base case: when we find a null
            if vals[self.i] == "N":
                # shift i forward
                self.i += 1
                # return null node
                return None

            # if not null then we have to create an actual tree node
            # gotta convert to integer value before we pass it in tho
            node = TreeNode(int(vals[self.i]))

            # shift i pointer forward
            self.i += 1

            # recursive preorder traversal shit
            node.left = dfs()
            node.right = dfs()

            # return root node we ended up creating
            return node

        # returning the tree (?)
        return dfs()
            
        
