class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

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