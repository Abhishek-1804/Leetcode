class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj = defaultdict(list)
        pre_to_crs = defaultdict(list)

        for x, y in prerequisites:
            adj[x].append(y)
            pre_to_crs[y].append(x)
        
        ans = []
        q = collections.deque([])

        for key, val in adj.items():
            if not val:
                q.append(key)
        
        while q:
            crs = q.popleft()
            ans.append(crs)

            if len(ans) == numCourses:
                return ans

            for i in pre_to_crs[crs]:
                adj[i].remove(crs)

                if not adj[i]:
                    q.append(i)
        
        return []

