# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # initialize empty array to collect things in preorder sequence
        res = []

        # define recursive helper that visits subtrees in preorder
        def dfs(node):
            # base case
            # when traversal hits an empty branch or missing child
            if not node:
                # append "N" to record absence of node
                res.append("N")

                # returns immediately to backtrack to the parent call frame
                return

            # preoder "visit" step 
            # append current node before exploring children
            res.append(str(node.val))

            # recursively explores entire left subtree to completion
            dfs(node.left)

            # recursively explores entire right subtree after left branch has fully resolved
            dfs(node.right)

        # kick off traversal starting at the root
        dfs(root)

        # flattens the array into a single comma seperated string
        return ",".join(res)   

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # splits the encoded string back into an
        # ordered list of strings tokens.
        vals = data.split(",")

        # sets pointer to track curr token in vals.
        # use self b/c allows recursive calls to advance a
        # shared index with passing pointer objects 
        # down and up the call stack.
        self.i = 0

        def dfs():
            # checks if curr token represents null node
            if vals[self.i] == "N":
                # consumes the "N" token by moving pointer
                # to next element.
                self.i += 1

                # returns None to attach as an empty child
                # to the caller.
                return None

            # recreates root of curr subtree 
            node = TreeNode(int(vals[self.i]))
            
            # consumes the curr value token, advancing the pointer
            # so the next recursive call reads the start of this
            # node's left subtree.
            self.i += 1

            # rebuilds the left subtree from subsequent tokens
            node.left = dfs()

            # rebuils the right subtree once the left subtree
            # has consumed all of its corresponding tokens
            node.right = dfs()

            # returns the assembled subtree up the call stack
            return node

        # returns the root of the reconstructred binary tree
        return dfs()
