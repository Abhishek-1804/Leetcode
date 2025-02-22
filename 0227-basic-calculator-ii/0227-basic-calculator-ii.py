class Solution:
    def calculate(self, s: str) -> int:
        num = 0
        pre_op = '+'
        stack = []

        for i, c in enumerate(s):
            if c.isdigit():
                num = num * 10 + int(c)
            if (not c.isdigit() and c != ' ') or i == len(s) - 1:
                if pre_op == '+':
                    stack.append(num)
                elif pre_op == '-':
                    stack.append(-num)
                elif pre_op == '*':
                    stack.append(stack.pop() * num)
                elif pre_op == '/':
                    stack.append(math.trunc(stack.pop() / num))
                pre_op = c
                num = 0
                
        return sum(stack)