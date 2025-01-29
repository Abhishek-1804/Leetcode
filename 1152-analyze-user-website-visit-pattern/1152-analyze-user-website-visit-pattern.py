class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        
        webInfo = []

        for u, t, w in zip(username, timestamp, website):
            webInfo.append((u, t, w))
        
        webInfo.sort(key=lambda x: x[1])

        websiteVisit = defaultdict(list)
        for u, t, w in webInfo:
            websiteVisit[u].append(w)
        
        possibleTuples = defaultdict(int)
        for usr in websiteVisit:
            webRoutes = set(combinations(websiteVisit[usr], 3))
            for webRoute in webRoutes:
                possibleTuples[webRoute] += 1

        maxVal, routes = max(possibleTuples.values()), []
        for r, val in possibleTuples.items():
            if val == maxVal:
                routes.append(r)
                
        if len(routes) > 1:
            # SORTS LEXICOGRAPHICALLY
            routes.sort()
        
        return routes[0]