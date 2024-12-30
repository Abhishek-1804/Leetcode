class Solution:
    def isValid(self, s: str) -> bool:
        
        h = {
            '(':')',
            '[':']',
            '{':'}'
        }

        stack = []

        for i in s:
            if i in h:
                stack.append(i)
            else:
                if stack and h[stack.pop()] == i:
                    continue
                return False
        
        return True if not stack else False