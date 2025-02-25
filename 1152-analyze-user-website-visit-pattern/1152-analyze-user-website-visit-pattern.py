class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        
        website_info = [[t, u, w] for u, t, w in zip(username, timestamp, website)]
        website_info.sort()
        
        h = {}

        for _, u, w in website_info:
            if u not in h:
                h[u] = []
            h[u].append(w)
        
        patterns = {}
        for key, val in h.items():
            if len(val) < 3:
                continue
            seen = set()
            for comb in combinations(val, 3):
                if comb not in seen:
                    patterns[comb] = patterns.get(comb, 0) + 1
                    seen.add(comb)
        
        max_count = max(patterns.values())
        best_pattern = min([pattern for pattern, count in patterns.items() if count == max_count])
        
        return list(best_pattern)