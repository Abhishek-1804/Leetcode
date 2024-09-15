class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        hmap = {}
        maxLen = 1

        for num in nums:
            if num not in hmap:
                left = hmap.get(num-1, 0)
                right = hmap.get(num+1, 0)
                total = 1 + left + right
                hmap[num-left] = total
                hmap[num+right] = total
                maxLen = max(maxLen, total)
        
        return maxLen