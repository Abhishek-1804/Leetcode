class Solution:
    def romanToInt(self, s: str) -> int:
        
        roman_to_int = {
            'I': 1,
            'IV': 4,
            'V': 5,
            'IX': 9,
            'X': 10,
            'XL': 40,
            'L': 50,
            'XC': 90,
            'C': 100,
            'CD': 400,
            'D': 500,
            'CM': 900,
            'M': 1000
            }
        
        ind = len(s) - 1
        res = 0

        while ind >= 0:
            if ind - 2 >= 0 and s[ind-1:ind+1] in roman_to_int:
                res += roman_to_int[s[ind-1:ind+1]]
                ind -= 2
            else:
                res += roman_to_int[s[ind]]
                ind -= 1
        
        return res