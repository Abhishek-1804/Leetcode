class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        digits = digits[::-1]

        carry = False
        start = 0

        while start < len(digits):
            if digits[start] != 9:
                digits[start] += 1
                start += 1
                return digits[::-1]
        
            else:
                if carry:
                    if digits[start] == 9:
                        digits[start] = 0
                        start += 1
                    else:
                        digits[start] += 1
                        carry = False
                        break
                
                else:
                    digits[start] = 0
                    carry = True
                    start += 1

        if carry:
            digits.append(1)
        
        return digits[::-1]