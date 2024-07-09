class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        d = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'
        }
        
        res = []

        def dfs(next_digits, curStr):
            if not next_digits: 
                res.append(curStr)
                return
        
            for c in d[digits[i]]:
                dfs(next_digits[1:], curStr+c)

        if digits:
            dfs(digits, "")

        return res