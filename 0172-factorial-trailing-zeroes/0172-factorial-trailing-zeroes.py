class Solution:
    def trailingZeroes(self, n: int) -> int:
        
        result = 0

        while n > 0:
            result += n//5
            n //= 5
        
        return result