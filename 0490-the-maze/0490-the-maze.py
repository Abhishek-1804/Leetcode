class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        rows, cols = len(maze), len(maze[0])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        stack = [tuple(start)]
        seen = set()
        
        while stack:
            x, y = stack.pop()
            if [x, y] == destination:
                return True
            if (x, y) in seen:
                continue
            seen.add((x, y))
            
            for dx, dy in directions:
                nx, ny = x, y
                # Roll the ball until it hits a wall or boundary
                while 0 <= nx + dx < rows and 0 <= ny + dy < cols and maze[nx + dx][ny + dy] == 0:
                    nx += dx
                    ny += dy
                stack.append((nx, ny))
        return False
