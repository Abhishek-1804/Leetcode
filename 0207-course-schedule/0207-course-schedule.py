class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj = {i: [] for i in range(numCourses)}
        
        # Building the adjacency list
        for crs, pre in prerequisites:
            adj[crs].append(pre)
        
        visited = set()
        def dfs(crs):
            if crs in visited:
                return False
            
            if adj[crs] == []:
                return True

            visited.add(crs)
            for neighbor in adj[crs]:
                if not dfs(neighbor): return False
            
            visited.remove(crs)
            adj[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        
        return True
