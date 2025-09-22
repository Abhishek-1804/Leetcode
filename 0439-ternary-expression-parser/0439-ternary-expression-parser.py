class Solution:
    def parseTernary(self, expression: str) -> str:

        stack = []
        is_cond = False  # set to True right after seeing '?'
        for c in reversed(expression):
            if c == ':':
                continue
            if c == '?':
                is_cond = True
                continue
            if is_cond:
                # c is the condition ('T' or 'F'); stack has [ ..., false_val, true_val ]
                true_val = stack.pop()
                false_val = stack.pop()
                stack.append(true_val if c == 'T' else false_val)
                is_cond = False
            else:
                stack.append(c)
        return stack.pop()