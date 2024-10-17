class Solution:
    def calculate(self, s: str) -> int:
        import re

        s = ''.join(s.split())
        s = re.split(r'(\+|\-|\*|/)', s)

        i = 0
        stack = []

        while i < len(s):
            if s[i].isnumeric():
                stack.append(int(s[i]))
                i += 1

            else:
                if s[i] == '+' or s[i] == '-':
                    stack.append(s[i])
                    i += 1
                
                elif s[i] == '/' and stack:
                    stack.append(int(stack.pop() / int(s[i+1])))
                    i += 2

                elif s[i] == '*' and stack:
                    stack.append(int(stack.pop() * int(s[i+1])))
                    i += 2
        
        stack = stack[::-1]
        ans = stack.pop()
        while stack:
            op = stack.pop()
            if op == '+':
                ans += stack.pop()
            else:
                ans -= stack.pop()
        
        return ans