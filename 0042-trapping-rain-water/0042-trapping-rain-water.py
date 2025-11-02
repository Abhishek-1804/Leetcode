class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []  # Store indices
        answer = 0
        
        for i in range(len(height)):
            # While current bar is taller than stack base
            while stack and height[i] > height[stack[-1]]:
                base = stack.pop()  # This is the bottom/valley
                
                if not stack:  # No left boundary
                    break
                
                # Distance between left and right boundaries
                distance = i - stack[-1] - 1
                
                # Water height is bounded by shorter wall minus valley depth
                bounded_height = min(height[i], height[stack[-1]]) - height[base]
                
                answer += distance * bounded_height
            
            stack.append(i)
        
        return answer
