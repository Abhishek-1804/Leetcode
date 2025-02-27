class Solution:
    def myPow(self, x: float, n: int) -> float:

        if n == 0:
            return 1

        if n < 0:
            x = 1/x
            n = -n

        ans = 1

        while n > 0:
            if n%2 == 0:
                n //= 2
                x *= x
            
            else:
                ans *= x
                n -= 1
        
        return ans