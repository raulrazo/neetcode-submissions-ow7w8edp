class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # create parent array
        # each node is going to be the parent of itself
        par = [i for i in range(n)]

        # list of ranks
        # each component is going to have a rank of 1 initially
        rank = [1] * n

        # we want to find its root parent
        def find(n1):
            res = n1

            # we know we can stop searching once we've gotten
            # to a node where the node itself is its own parent
            # because that means we cant't go any higher
            # and we found the root and that is why our 
            # return statement is the way it is
            while res != par[res]:
                # idea: path compression
                # before we go to the parent, we want to set the parent
                # of result = its grandparent
                # set our parent to the parent of our parent if it
                # happens to exist, this makes the chain shorter
                # if we do not have a grandparent then this does nothing
                par[res] = par[par[res]]

                # update the current pointer to be its parent
                res = par[res]

            return res

        # take two nodes and union their components together
        def union(n1, n2):
            # find the root parents of each of the nodes
            p1, p2 = find(n1), find(n2)

            # if they have the same parent, we return immediately
            # to indicate that we did perform a union
            if p1 == p2:
                return 0

            # doing the union by rank
            if rank[p2] > rank[p1]:
                # p2 is going to be the parent of p1
                par[p1] = p2

                # increase the rank of p2 because we just added
                # some children to it
                rank[p2] += rank[p1]
            else:
                # doing the exact opposite of above
                par[p2] = p1
                rank[p1] += rank[p2]

            # return 1 to indicate we did a union
            return 1

        # go thru every single edge
        # initial components is n so we set result to n
        res = n
        for n1, n2 in edges:
            # union n1 and n2 together
            # everytime we perform a succesful union, we want to
            # decrement the result by 1
            # if no union then we return 0 and result is not updated

            res -= union(n1, n2)

        return res


        