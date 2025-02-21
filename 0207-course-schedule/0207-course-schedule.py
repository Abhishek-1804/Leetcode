class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        pre_to_crs = {i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            pre_to_crs[pre].append(crs)

        seen = set()
        
        def has_cycle(key):
            if not pre_to_crs[key]:
                return False
            
            if key in seen:
                return True
            
            seen.add(key)
            for neighbor in pre_to_crs[key]:
                if has_cycle(neighbor):
                    return True
            seen.remove(key)
            pre_to_crs[key] = []
            return False
            
        for key, val in pre_to_crs.items():
            if has_cycle(key):
                return False
        
        return True

    def canFinish_bfs(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        pre_to_crs = {pre:[] for pre in range(numCourses)}

        # tracking number of prereqs for courses
        indegree = [0]*numCourses

        for crs, pre in prerequisites:
            pre_to_crs[pre].append(crs)
            indegree[crs] += 1

        q = deque([])
        for crs in range(len(indegree)):
            if indegree[crs] == 0:
                q.append(crs)
        
        while q:
            pre = q.popleft()
            for crs in pre_to_crs[pre]:
                indegree[crs] -= 1
                if indegree[crs] == 0:
                    q.append(crs)
        
        for crs in indegree:
            if crs != 0:
                return False
        
        return True