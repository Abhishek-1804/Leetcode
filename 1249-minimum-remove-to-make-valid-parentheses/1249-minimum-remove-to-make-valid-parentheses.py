class Solution:
    def minRemoveToMakeValid_2(self, s: str) -> str:

        d = {}
        stack = []

        for i in range(len(s)):
            if s[i].isalpha():
                d[i] = s[i]
            else:
                if s[i] == ')':
                    if not stack:
                        continue
                    else:
                        stack.pop()
                        d[i] = ')'
                else:
                    stack.append(i)
                    d[i] = '('
        
        while stack:
            ind = stack.pop()
            del d[ind]

        ans = ''
        for key, val in d.items():
            ans += val
        
        return ans

    def minRemoveToMakeValid(self, s: str) -> str:

        a = ''
        open_count = 0

        for i in range(len(s)):
            if s[i].isalpha():
                a += s[i]
            else:
                if s[i] == ')':
                    if open_count:
                        a += s[i]
                        open_count -= 1
                    else:
                        continue
                else:
                    open_count += 1
                    a += s[i]

        final_ans = ''
        for i in a[::-1]:
            if open_count and i == '(':
                open_count -= 1
            else:
                final_ans += i
        
        return final_ans[::-1]