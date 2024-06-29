class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj = {}

        for crs, pre in prerequisites:
            if crs not in adj:
                adj[crs] = []
            adj[crs].append(pre)
        
        visited = set()
        def dfs(crs):
            if crs in visited:
                return False

            if crs not in adj or adj[crs] == []:
                return True
            
            visited.add(crs)
            for neighbor in adj[crs]:
                if not dfs(neighbor): return False
            
            visited.remove(crs)
            adj[crs] = []
            return True
        
        for crs in adj:
            if not dfs(crs): return False
        
        return True