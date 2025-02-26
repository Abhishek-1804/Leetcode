class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        
        arr = []
        for i, row in enumerate(grid):
            if limits[i]:
                arr.extend(sorted(row, reverse=True)[:limits[i]])
        return sum(sorted(arr, reverse=True)[:k])