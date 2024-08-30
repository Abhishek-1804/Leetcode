class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        hmap = {}

        for dependent, independent in prerequisites:
            if dependent not in hmap:
                hmap[dependent] = []
            if independent not in hmap:
                hmap[independent] = []
            hmap[dependent].append(independent)

        visited = set()

        def dfs(course):
            if not hmap[course]:
                return True
            if course in visited:
                return False
            
            visited.add(course)
            for i in hmap[course]:
                if not dfs(i):
                    return False
            visited.remove(course)
            hmap[course] = []
            return True
            

        for dependent, independent in prerequisites:
            if not dfs(dependent):
                return False

        return True