class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        
        while left < right:
            mid = (left + right) // 2
            total_hrs = sum(math.ceil(x / mid) for x in piles)

            if total_hrs > h:  # Too slow, increase speed
                left = mid + 1
            else:  # Try a lower speed
                right = mid
        
        return left