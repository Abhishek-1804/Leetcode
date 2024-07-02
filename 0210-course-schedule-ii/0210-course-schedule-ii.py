class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj = {i:[] for i in range(numCourses)}

        for x,y in prerequisites:
            adj[x].append(y)

        ans = []
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
            ans.append(crs)
            return False
        
        for crs in range(numCourses):
            if hasCycle(crs):
                return []
            
        return ans
