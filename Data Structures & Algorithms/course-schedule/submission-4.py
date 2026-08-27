class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = { c : [] for c in range(numCourses) }

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        cycle = set()

        def dfs(crs):
            if crs in cycle:
                return False

            if preMap[crs] == []:
                return True

            cycle.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre):
                    return False

            cycle.remove(crs)

            preMap[crs] = []

            return True 

        for crs in range(numCourses):
            if not dfs(crs):
                return False 

        return True