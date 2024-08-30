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

        def has_cycle(course):
            if not hmap[course]:
                return False

            if course in visited:
                return True
            
            visited.add(course)
            for i in hmap[course]:
                if has_cycle(i):
                    return True

            visited.remove(course)
            return False

        for dependent, independent in prerequisites:
            if has_cycle(dependent):
                return False

        return True