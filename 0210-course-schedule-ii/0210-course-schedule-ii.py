class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        ans = []

        adj = {i:[] for i in range(numCourses)}

        for crs in prerequisites:
            adj[crs[0]].append(crs[1])
        
        status = [0] * numCourses
        def hasCycle(crs):
            if status[crs] == -1:
                return True
            
            if status[crs] == 2:
                return False

            status[crs] = -1
            for pre in adj[crs]:
                if hasCycle(pre):
                    return True
            
            status[crs] = 2
            ans.append(crs)
            return False
            

        for i in range(numCourses):
            if hasCycle(i):
                return []
        
        return ans