class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        p_s = [[p, s] for p, s in zip(position, speed)]
        p_s.sort(reverse = True, key = lambda x: x[0])

        stack = []

        for p, s in p_s:
            stack.append((target - p) // s)
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)