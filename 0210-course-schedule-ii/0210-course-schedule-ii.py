class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
                
        adj = {i:set() for i in range(numCourses)}
        pre_to_crs = collections.defaultdict(set) 

        for x,y in prerequisites:
            adj[x].add(y)
            pre_to_crs[y].add(x)
        
        q = collections.deque([])
        for crs, pre in adj.items():
            if len(pre) == 0:
                q.append(crs)
        
        ans = []
        while q:
            course = q.popleft()
            ans.append(course)

            if len(ans) == numCourses:
                return ans

            for crs in pre_to_crs[course]:

                adj[crs].remove(course)

                if not adj[crs]:
                    q.append(crs)
        
        return []
