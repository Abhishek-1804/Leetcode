class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        h = {}
        max_len = 0

        for num in nums:
            if num not in h:
                left = h.get(num-1, 0)
                right = h.get(num+1, 0)
                total = 1 + left + right

                h[num] = total
                h[num - left] = total
                h[num + right] = total
                
                max_len = max(max_len, total)
        
        return max_len