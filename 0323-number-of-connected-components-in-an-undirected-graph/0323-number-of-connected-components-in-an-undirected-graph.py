class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        from collections import defaultdict
        
        connections = defaultdict(list)
        for u, v in edges:
            connections[u].append(v)
            connections[v].append(u)  # undirected edge

        seen = set()
        answer = 0

        for node in range(n):  # Loop over all nodes to catch isolated ones too
            if node in seen:
                continue
            stack = [node]
            while stack:
                k = stack.pop()
                if k in seen:
                    continue  # not break!
                seen.add(k)
                for neighbor in connections[k]:
                    stack.append(neighbor)  # add each neighbor
            answer += 1
        return answer
