from heapq import heappop, heappush

class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        heap = [(0, start[0], start[1])]
        distances = [[float('inf')] * cols for _ in range(rows)]
        distances[start[0]][start[1]] = 0

        while heap:
            dist, r, c = heappop(heap)
            if [r, c] == destination:
                return dist

            for dr, dc in directions:
                nr, nc, steps = r, c, 0
                # Roll until wall or boundary
                while 0 <= nr + dr < rows and 0 <= nc + dc < cols and maze[nr + dr][nc + dc] == 0:
                    nr += dr
                    nc += dc
                    steps += 1
                if dist + steps < distances[nr][nc]:
                    distances[nr][nc] = dist + steps
                    heappush(heap, (dist + steps, nr, nc))

        return -1
