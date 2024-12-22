class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        ans = float('-inf')

        start = 0
        end = len(height) - 1

        while start < end:
            ans = max(ans, (end-start)*min(height[start], height[end]))
            
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1

        return ans