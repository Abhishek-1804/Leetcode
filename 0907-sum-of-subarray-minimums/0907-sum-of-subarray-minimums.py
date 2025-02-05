class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)
        
        # number of subarrays where arr[i] is min on the left side
        left = [0] * n
        # number of subarrays where arr[i] is min on the right side
        right = [0] * n
        
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()

            left[i] = i + 1 if not stack else i - stack[-1]
            stack.append(i)
        
        stack = []
        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            
            right[i] = n - i if not stack else stack[-1] - i
            stack.append(i)
        
        result = 0
        for i in range(n):
            result = (result + arr[i] * left[i] * right[i]) % MOD
        
        return result
        