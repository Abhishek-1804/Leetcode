class Solution:
    def isValid(self, s: str) -> bool:
        
        h = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }

        stack = []

        for i in s:
            if i in h:
                stack.append(i)
            elif not stack or h[stack.pop()] != i:
                    return False
        
        return True if not stack else False
