class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        start = 0
        end = len(matrix)-1

        while start <= end:
            mid = (start+end) // 2

            if matrix[mid][0] <= target <= matrix[mid][-1]:
                break
            elif target > matrix[mid][-1]:
                start = mid + 1
            else:
                end = mid - 1
        
        row = mid

        start = 0
        end = len(matrix[0]) - 1

        while start <= end:
            mid = (start + end) // 2
            mid_number = matrix[row][mid]

            if target == mid_number:
                return True
            elif target < mid_number:
                end = mid - 1
            else:
                start = mid + 1
        
        return False