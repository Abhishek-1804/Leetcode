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
                if i == 31:  # Handle the sign bit for negative numbers
                    result -= (1 << i)
                else:
                    result |= (1 << i)

        return result