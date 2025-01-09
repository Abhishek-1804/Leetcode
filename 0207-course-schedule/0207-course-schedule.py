class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj = {i:[] for i in range(numCourses)}

        for crs in prerequisites:
            adj[crs[1]].append(crs[0])

        seen = set()
        
        def has_cycle(key):
            if not adj[key]:
                return False
            
            if key in seen:
                return True
            
            seen.add(key)
            for neighbor in adj[key]:
                if has_cycle(neighbor):
                    return True
            seen.remove(key)
            adj[key] = []
            return False
            
        for key, val in adj.items():
            if has_cycle(key):
                return False
        
        return True