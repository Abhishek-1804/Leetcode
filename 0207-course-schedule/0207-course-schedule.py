class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj = {i:[] for i in range(numCourses)}

        for x,y in prerequisites:
            adj[x].append(y)

        state = [0]*numCourses
        def hasCycle(crs):
            if state[crs] == 1:
                return False
            
            if state[crs] == -1:
                return True

            state[crs] = -1
            for neighbor in adj[crs]:
                if hasCycle(neighbor):
                    return True
            
            state[crs] = 1
            return False
        
        for crs in range(numCourses):
            if hasCycle(crs):
                return False
            
        return True