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
                return False
            if course in visited:
                return True
            
            visited.add(course)
            for i in hmap[course]:
                if dfs(i):
                    return True
            visited.remove(course)
            hmap[course] = []
            return False

        for dependent, independent in prerequisites:
            if dfs(dependent):
                return False

        return True