class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            flag = False
            while stack and a < 0 and stack[-1] > 0:
                if stack[-1] < abs(a):
                    stack.pop()
                elif stack[-1] >= abs(a):
                    flag = True
                    if stack[-1] == abs(a):
                        stack.pop()
                    break

            if not flag:
                stack.append(a)
                
        return stack