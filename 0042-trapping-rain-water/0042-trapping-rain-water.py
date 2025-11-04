class Solution:
    def trap(self, height: List[int]) -> int:
        return self.trap_stack(height)

    def trap_stack(self, height: List[int]) -> int:

        answer = 0

        # stores indicies
        stack = []

        for i in range(len(height)):

            while stack and height[i] >= height[stack[-1]]:
                base = stack.pop()

                if not stack:
                    break
                
                left = stack[-1]
                distance = i - left - 1
                bounded_height = min(height[i], height[left]) - height[base]
                answer += distance * bounded_height

            # for decreasing heights
            stack.append(i)
        
        return answer
