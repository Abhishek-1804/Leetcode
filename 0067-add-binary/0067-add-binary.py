class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        result = ''
        carry = 0

        a_end = len(a) - 1
        b_end = len(b) - 1

        while a_end >= 0 or b_end >= 0 or carry:

            if a_end >= 0:
                carry += int(a[a_end])
                a_end -= 1
            
            if b_end >= 0:
                carry += int(b[b_end])
                b_end -= 1
            
            result += str(carry % 2)
            carry //= 2
        
        return result[::-1]