class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        bits = [0]*32

        for num in nums:
            for i in range(32):
                bits[i] += num & (1 << i)
        
        result = 0
        for i in range(32):
            if bits[i]%3 != 0:
                result |= (1<<i)
        
        if bits[31]%3 != 0:
            result -= 1 << 32
        
        return result
