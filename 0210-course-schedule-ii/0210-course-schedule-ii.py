class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
                 
        adj = {i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            adj[crs].append(pre)
        
        cycle = set()
        visit = set()
        ans = []
        
        def has_cycle(crs):
            if crs in cycle:
                return True
            if crs in ans:
                return False
            
            cycle.add(crs)
            for i in adj[crs]:
                if has_cycle(i):
                    return True

            cycle.remove(crs)
            ans.append(crs)
            return False
        
        for crs in range(numCourses):
            if has_cycle(crs):
                return []
        
        return ans
