class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        from collections import defaultdict
        
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
        
        states = [0]*n

        def dfs(node):
            if states[node] == 1:
                return False
            if states[node] == 2:
                return True
            if not graph[node]:
                return node == destination
            
            states[node] = 1
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            
            states[node] = 2
            return True
        
        return dfs(source)