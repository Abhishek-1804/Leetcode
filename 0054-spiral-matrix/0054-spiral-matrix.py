class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
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

