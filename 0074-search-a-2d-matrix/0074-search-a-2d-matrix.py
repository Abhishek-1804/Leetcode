class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        row_low = 0
        row_high = len(matrix) - 1
        col_low = 0
        col_high = len(matrix[0]) - 1

        while row_low < row_high:
            row_mid = (row_low + row_high) // 2
        
            if target >= matrix[row_mid][0] and target <= matrix[row_mid][-1]:
                # The target is within the range of this row
                row_low = row_mid
                break
            elif target < matrix[row_mid][0]:
                row_high = row_mid - 1
            else:
                row_low = row_mid + 1
        
        while col_low <= col_high:
            col_mid = (col_low + col_high) // 2
            
            if target == matrix[row_low][col_mid]:
                return True
            
            elif target > matrix[row_low][col_mid]:
                col_low = col_mid + 1
            
            else:
                col_high = col_mid - 1
        
        return False