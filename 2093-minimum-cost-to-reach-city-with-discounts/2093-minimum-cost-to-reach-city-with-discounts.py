class Solution:
    def minimumCost(self, n: int, highways: List[List[int]], discounts: int) -> int:
        import heapq
        
        adj_graph = {}

        for c1, c2, toll in highways:
            if c1 not in adj_graph:
                adj_graph[c1] = []
            if c2 not in adj_graph:
                adj_graph[c2] = []
            
            adj_graph[c1].append((c2, toll))
            adj_graph[c2].append((c1, toll))
        
        dist = [[float('inf')] * (discounts+1) for _ in range(n)]
        dist[0][0] = 0
        
        q = [(0, 0, 0)]  # cost, city, discounts_used

        while q:
            cost, city, discounts_used = heapq.heappop(q)

            if city == n - 1:
                return cost

            if city not in adj_graph:
                continue
            
            for neighbor, toll in adj_graph[city]:
                # Without discount
                new_cost = cost + toll
                if new_cost < dist[neighbor][discounts_used]:
                    dist[neighbor][discounts_used] = new_cost
                    heapq.heappush(q, (new_cost, neighbor, discounts_used))
                
                # With discount (if available)
                if discounts_used < discounts:
                    discounted_cost = cost + toll // 2
                    if discounted_cost < dist[neighbor][discounts_used + 1]:
                        dist[neighbor][discounts_used + 1] = discounted_cost
                        heapq.heappush(q, (discounted_cost, neighbor, discounts_used + 1))
        
        return -1
