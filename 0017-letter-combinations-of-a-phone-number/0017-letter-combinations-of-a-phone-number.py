class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        
        h = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "j", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        output = []

        def backtrack(temp_str, start):
            if len(temp_str) == len(digits):
                output.append(temp_str)
                return
            
            for i in h[digits[start]]:
                backtrack(temp_str + i, start + 1)
            
        if not digits:
            return output

        backtrack("", 0)

        return output