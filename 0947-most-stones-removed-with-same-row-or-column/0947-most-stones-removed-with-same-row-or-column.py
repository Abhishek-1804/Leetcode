class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:

        def dfs(x, y):
            nonlocal seen
            seen.add((x, y))
            for nx, ny in stones:
                if (nx, ny) not in seen:
                    if nx == x or ny == y:  # Connected if they share the same row or column
                        dfs(nx, ny)

        seen = set()
        num_islands = 0

        for x, y in stones:
            if (x, y) not in seen:
                dfs(x, y)
                num_islands += 1

        return len(stones) - num_islands
