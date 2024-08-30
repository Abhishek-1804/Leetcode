class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj = {i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            adj[crs].append(pre)
        
        visited = set()
        
        def has_cycle(crs):
            if not adj[crs]:
                return False

            if crs in visited:
                return True

            visited.add(crs)
            for i in adj[crs]:
                if dfs(i):
                    return True

            visited.remove(crs)
            adj[crs] = []
            return False           

        
        for crs, pre in prerequisites:
            if has_cycle(crs):
                return False
        
        return True