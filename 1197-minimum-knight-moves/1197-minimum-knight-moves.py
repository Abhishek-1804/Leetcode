class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        x, y = abs(x), abs(y)
        if (x < y): x, y = y, x
        if (x == 1 and y == 0): return 3        
        if (x == 2 and y == 2): return 4 
        delta = x - y
        if (y > delta): return delta - 2 * int((delta - y) // 3)
        else: return delta - 2 * int((delta - y) // 4)

    def minKnightMoves_bfs(self, x: int, y: int) -> int:
        # the offsets in the eight directions
        offsets = [(1, 2), (2, 1), (2, -1), (1, -2),
                   (-1, -2), (-2, -1), (-2, 1), (-1, 2)]

        def bfs(x, y):
            visited = set()
            queue = deque([(0, 0)])
            steps = 0

            while queue:
                curr_level_cnt = len(queue)
                # iterate through the current level
                for i in range(curr_level_cnt):
                    curr_x, curr_y = queue.popleft()
                    if (curr_x, curr_y) == (x, y):
                        return steps

                    for offset_x, offset_y in offsets:
                        next_x, next_y = curr_x + offset_x, curr_y + offset_y
                        if (next_x, next_y) not in visited:
                            visited.add((next_x, next_y))
                            queue.append((next_x, next_y))

                # move on to the next level
                steps += 1

        return bfs(x, y)