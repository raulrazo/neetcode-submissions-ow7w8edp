class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # build prereq map
        prereqs = { c : [] for c in range(numCourses) }

        # initialize output list for order of classes
        output = []

        # populate prereq map
        for crs, pre in prerequisites:
            prereqs[crs].append(pre)

        # create visit and cycle sets
        visit = set()
        cycle = set()

        # define dfs function
        def dfs(crs):
            # check if this node is part of a cycle
            if crs in cycle:
                # return False / no bueno
                return False

            # check if node is visisted
            if crs in visit:
                # return True / we good just skip this 
                return True

            # if node not in cycle or visit yet
            # then let's add it to our current cycle
            cycle.add(crs)

            # now we recursive call dfs 
            # for the prereqs of this node
            # or the nodes this node has edges to
            for pre in prereqs[crs]:
                # if one of our nodes is in the same cycle 
                # then dfs will return false
                # and we want this to return false
                if dfs(pre) == False:
                    return False

            # if none of our prereqs were in the same cycle
            # then we can remove this node from cycle
            cycle.remove(crs)

            # add this node to visited
            visit.add(crs)

            # and add this node to our current order of classes
            output.append(crs)

        # call dfs on all nodes
        for crs in range(numCourses):
            if dfs(crs) == False:
                # if we detect a cycle at any point,
                # then we can automatically
                # return empty array
                return []

        # if we didn't, then we return output list we built
        return output
        