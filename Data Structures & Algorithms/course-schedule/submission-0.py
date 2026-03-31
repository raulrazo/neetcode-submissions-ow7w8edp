class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # create our adjacency list
        # for every course initially, we want to map it to an empty list
        preMap = {i:[] for i in range(numCourses)}
        
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # visitSet = all courses along the curr DFS path
        visitSet = set()

        def dfs(crs):
            # base case: if crs is in visitSet
            if crs in visitSet:
                # we detected a loop so return False
                return False

            # base case: if prereqs for this crs are an empty list
            if preMap[crs] == []:
                # tell us that this course can be completed so we can return True
                return True

            # take this crs and add it to our visitSet
            visitSet.add(crs)

            # loop through prereqs of this crs
            for pre in preMap[crs]:
                # run dfs on this prereq
                if not dfs(pre): return False

            # remove crs from visitSet because we done visiting
            visitSet.remove(crs)

            # since we know this course can be visited, we can set preMap to empty list
            # so that if we ever have to run DFS on it again, we can return True immediately because of base case 
            preMap[crs] = []

            # if that if statement does not execute this means this course can be taken
            # so we want to return True
            return True

        # call DFS for all of our courses
        for crs in range(numCourses):
            if not dfs(crs): return False

        # if that shit didn't execute that it is possible to complete all courses
        return True
