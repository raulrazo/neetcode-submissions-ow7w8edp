class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # build adjacency list of prereqs
        # for every course, map it to an empty list
        prereq = { c:[] for c in range(numCourses) }

        # fill in the prereq map
        # for every course, prereq pair in our prereq list
        for crs, pre in prerequisites:
            # add the prereq of this course to our list
            prereq[crs].append(pre)


        # a course has 3 possible states:

        # visited -> crs has been added to output
        # visiting -> crs has not been added to output, but added to cycle
        # unvisited -> crs not added to output or cycle

        # create output list
        output = []

        # create to sets to let us know if a node or course has already been visited
        # or if it's currently along the given path
        visit = set()
        cycle = set()

        # define DFS function
        # pass in course number that we're currently visiting
        def dfs(crs):
            # first thing: detect a cycle
            # if this crs is already inside of cycle set
            # that means we're visiting twice
            # that means we've detected a cycle
            if crs in cycle:
                # that means we return False and terminate algorithm
                return False

            # if crs has already been visited
            # that means we don't need to visit it twice
            # so we return True

            if crs in visit:
                return True


            # add this crs to our cycle
            cycle.add(crs)

            # recursively run DFS
            # go thru every prereq of this course
            for pre in prereq[crs]:
                # run recursively DFS on this prereq
                # and if that returns false,
                # we know we just detected a cycle
                if dfs(pre) == False:
                    # so we also return False
                    return False

                # if it equals true, then we continue
                # to go thru all the prereqs

            # remove the crs b/c it is no longer along the path that we're going
            cycle.remove(crs)

            # add it to visit set b/c we just visited it
            visit.add(crs)

            # since this crs has been visited, we can add it to our output list
            # we can only add a crs after we add its prereqs
            # and we know we added them at this point because recursive DFS loop

            output.append(crs)

            # return True, everything was fine
            return True

        # go thru every course
        for c in range(numCourses):
            # run dfs on every single course 
            # but check if return value of any of these courses
            # is False, meaning we detected cycle
            # so we are forced to return an empty list
            if dfs(c) == False:
                return []

            # if DFS doesn't detect cycle
            # then loop finish running and we can return the output list we built

        return output

        