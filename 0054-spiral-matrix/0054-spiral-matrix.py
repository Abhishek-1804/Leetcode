class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # return self.spiralOrder_cleaner(matrix)
        return self.spiralOrder_verbose(matrix)
    
    def spiralOrder_cleaner(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])
        x, y, dx, dy = 0, 0, 1, 0
        res = []

        for _ in range(rows * cols):
            res.append(matrix[y][x])
            matrix[y][x] = "."

            if not 0 <= x + dx < cols or not 0 <= y + dy < rows or matrix[y+dy][x+dx] == ".":
                dx, dy = -dy, dx
            
            x += dx
            y += dy
        
        return res

    def spiralOrder_verbose(self, matrix: List[List[int]]) -> List[int]:
        
        ans = []
        seen = set()

        row, col = 0, 0

        while len(seen) < len(matrix) * len(matrix[0]):

            while col < len(matrix[0]) and (row, col) not in seen:
                ans.append(matrix[row][col])
                seen.add((row, col))
                col += 1
            
            col -= 1
            row += 1
            while row < len(matrix) and (row, col) not in seen:
                ans.append(matrix[row][col])
                seen.add((row, col))
                row += 1
            
            row -= 1
            col -= 1
            while col >= 0 and (row, col) not in seen:
                ans.append(matrix[row][col])
                seen.add((row, col))
                col -= 1
            
            col += 1
            row -= 1
            while row >= 0 and (row, col) not in seen:
                ans.append(matrix[row][col])
                seen.add((row, col))
                row -= 1
            
            row += 1
            col += 1
        
        return ans

