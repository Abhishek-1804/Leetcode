class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        
        result = []
        
        # Handle negative sign
        if (numerator < 0) ^ (denominator < 0):
            result.append("-")
        
        numerator, denominator = abs(numerator), abs(denominator)
        
        # Integer part
        result.append(str(numerator // denominator))
        remainder = numerator % denominator
        
        if remainder == 0:
            return "".join(result)
        
        result.append(".")
        
        # Track remainder positions
        remainder_map = {}
        
        while remainder != 0:
            if remainder in remainder_map:
                # Insert '(' at the start of repeating part
                result.insert(remainder_map[remainder], "(")
                result.append(")")
                break
            
            # Store position BEFORE processing
            remainder_map[remainder] = len(result)
            
            remainder *= 10
            result.append(str(remainder // denominator))
            remainder %= denominator
        
        return "".join(result)
