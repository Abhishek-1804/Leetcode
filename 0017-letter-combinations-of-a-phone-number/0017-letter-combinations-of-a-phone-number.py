class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        hmap = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        output = []

        def backtrack(temp_str, i):
            if len(temp_str) == len(digits):
                output.append(temp_str)
                return
            
            for c in hmap[digits[i]]:
                backtrack(temp_str + c, i+1)
        
        if digits:
            backtrack("", 0)

        return output