"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # need a single data structure, hashmap
        oldToNew = {}

        # could call this clone
        # because we are taking the orignal node
        # and creating a clone of that node
        # and we are cloning all of its neighbors recursively
        # and the neighbors we are creating we are adding them to
        # the list of neighbors of this node
        def dfs(node):
            # if node in hashmap, then we already made a clone of it
            if node in oldToNew:
                # then we are just going to return that clone
                return oldToNew[node]

            # if clone doesn't exist then let's create it
            copy = Node(node.val)

            # add copy to hashmap
            oldToNew[node] = copy

            # then we want to make copies of every single neighbor of the original node
            for neighbor in node.neighbors:
                # run dfs on that neighbor
                # that is going to return the copy we ended up creating
                # and with that copy, we are going to take its list of neighbors
                # and append to that list of neighbors the return from this dfs (?)
                copy.neighbors.append(dfs(neighbor))

            # once we are doing getting all the copies of the neighbors
            # then we can return the copy we just made in this function call
            return copy

        # original node could be null
        return dfs(node) if node else None




        