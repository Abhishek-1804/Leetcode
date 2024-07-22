class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        bits_count = [0] * 32

        for num in nums:
            for i in range(32):
                if num & (1 << i):
                    bits_count[i] += 1

        result = 0
        for i in range(32):
            if bits_count[i] % 3 != 0:
                result |= (1 << i)
         
        return result