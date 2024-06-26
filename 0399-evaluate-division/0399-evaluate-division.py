from collections import deque
from typing import List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        graph = {}

        for (u,v), val in zip(equations, values):
            if u not in graph:
                graph[u] = {}
            if v not in graph:
                graph[v] = {}
            
            graph[u][v] = val
            graph[v][u] = 1/val

        def bfs(src, target):

            if src not in graph or target not in graph:
                return -1
            
            q, visit = deque(), set()
            q.append([src, 1])
            visit.add(src)
            
            while q:
                n, w = q.popleft()
                if n == target:
                    return w
                
                for neighbor, weight in graph[n].items():
                    if neighbor not in visit:
                        q.append([neighbor, w*weight])
                        visit.add(neighbor)

            return -1
        
        return [bfs(q[0], q[1]) for q in queries]