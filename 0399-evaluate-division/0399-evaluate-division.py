class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        hmap = {}

        for i in range(len(equations)):
            if equations[i][0] not in hmap:
                hmap[equations[i][0]] = {}
            if equations[i][1] not in hmap:
                hmap[equations[i][1]] = {}
            hmap[equations[i][0]][equations[i][1]] = values[i]
            hmap[equations[i][1]][equations[i][0]] = 1/values[i]
        
        def bfs(src, target):
            q = collections.deque([])
            seen = set()
            q.append([src, 1])

            while q:
                node, ans = q.popleft()
                if node not in hmap:
                    continue
                if node == target:
                    return ans
                for key, val in hmap[node].items():
                    if key not in seen:
                        seen.add(key)
                        q.append([key, val*ans])
            
            return -1
        
        return [bfs(q[0], q[1]) for q in queries]