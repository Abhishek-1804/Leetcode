class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        
        webInfo = []
        for u, t, w in zip(username, timestamp, website):
            webInfo.append((u, t, w))
        
        webInfo.sort(key=lambda x : x[1])

        visits = defaultdict(list)
        for u, _, w in webInfo:
            visits[u].append(w)
        
        possibleTuples = defaultdict(int)
        for u in visits:
            webRoutes = set(combinations(visits[u], 3))
            for webRoute in webRoutes:
                possibleTuples[webRoute] += 1
        
        maxVal, routes = max(possibleTuples.values()), []
        for r, val in possibleTuples.items():
            if maxVal == val:
                routes.append(r)
        
        if len(routes) > 1:
            routes.sort()
        
        return routes[0]