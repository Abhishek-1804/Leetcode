class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        
        ans = 0

        for i in range(1, n+1):
            if n % i == 0:
                ans += 1
            if ans == k:
                return i
        
        return -1