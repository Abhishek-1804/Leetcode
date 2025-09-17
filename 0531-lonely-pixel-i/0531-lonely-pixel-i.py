class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        rows = len(picture)
        cols = len(picture[0])
        
        # Count black pixels in each row and column
        row_counts = [0] * rows
        col_counts = [0] * cols
        
        # First pass: count black pixels
        for i in range(rows):
            for j in range(cols):
                if picture[i][j] == 'B':
                    row_counts[i] += 1
                    col_counts[j] += 1
        
        # Second pass: count lonely pixels
        lonely_count = 0
        for i in range(rows):
            for j in range(cols):
                if picture[i][j] == 'B' and row_counts[i] == 1 and col_counts[j] == 1:
                    lonely_count += 1
                    
        return lonely_count
