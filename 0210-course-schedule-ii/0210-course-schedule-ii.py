class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj_list = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            adj_list[crs].append(pre)
        
        output = []
        # 0 unvisited, 1 visiting, 2 visited
        state = [0] * numCourses

        def hasCycle(i):
            if state[i] == 1:
                return True
            
            if state[i] == 2:
                return False
            
            state[i] = 1
            for neighbor in adj_list[i]:
                if hasCycle(neighbor):
                    return True
            
            state[i] = 2
            output.append(i)
            return False
        
        for i in adj_list:
            if hasCycle(i):
                return []
        
        return output