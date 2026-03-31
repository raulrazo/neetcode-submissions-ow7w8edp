class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # edge case: we aren't given any nodes at all so return True
        # because an empty graph does count as a Tree
        if not n:
            return True

        # create adjacency list
        # for every single node in our input
        # we are going to create a pair in our hashmasp
        # and each pair is going to be value of that node
        # and an empty list
        adj = { i:[] for i in range(n) }

        # go thru every pair of nodes in every edge
        for n1, n2 in edges:
            # update adjacency list for the nodes
            adj[n1].append(n2)
            adj[n2].append(n1)

        # keep track of all the nodes we've visted
        visit = set()

        # i will be the value of the node we are visiting
        # prev is previous node that we came from
        def dfs(i, prev):
            # if node has already been visited, then we detected a loop
            if i in visit:
                # so return false
                return False

            # i hasn't been visited so let's add i
            visit.add(i)

            # go thru every single neighbor of i using adj list
            for j in adj[i]:
                # if we find node that we came from
                if j == prev:
                    # skip this iteration of the loop
                    continue

                # call dfs on this node with prev value i
                # because that's where we are coming from
                if not dfs(j, i):
                    # return False because we detected a loop
                    return False

            # we went thru all the neighbors and did not detect a loop
            return True

        # return the result
        # -1 b/c it will never exist in our graph
        # dfs handles loop detection, n == handles if they are all connected
        return dfs(0, -1) and n == len(visit)
