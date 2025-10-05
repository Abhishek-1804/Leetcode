import math

class Solution:
    def isArmstrong(self, n: int) -> bool:
        
        total = 0
        temp = n
        k_digits = len(str(n))

        while temp:
            val = temp%10
            total += math.pow(val, k_digits)
            temp //= 10
        
        return total == n