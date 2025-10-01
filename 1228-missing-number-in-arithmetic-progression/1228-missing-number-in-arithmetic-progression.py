class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        
        output = 0
        
        arr.sort()
        diff = abs(arr[-1] - arr[0]) // len(arr)

        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] != diff:
                output = arr[i-1] + diff
                return output
        
        return output