class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:

        len_s = len(s)
        
        for direction, amount in shift:
            mod_amount = amount % len_s

            if direction == 0:
                s = s[mod_amount:] + s[:mod_amount]
            else:
                s = s[len_s - mod_amount:] + s[:len_s - mod_amount]
        
        return s