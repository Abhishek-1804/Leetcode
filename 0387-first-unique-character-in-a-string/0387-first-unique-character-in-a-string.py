class Solution:
    def firstUniqChar(self, s: str) -> int:

        states = [0] * 26

        for i in s:
            # for capital letters
            if 65 <= ord(i) <= 90:
                if states[ord(i)-65] == 0:
                    states[ord(i)-65] = 1
                elif states[ord(i)-65] == 1:
                    states[ord(i)-65] = 2
                else:
                    continue
            
            else:
                if states[ord(i)-97] == 0:
                    states[ord(i)-97] = 1
                elif states[ord(i)-97] == 1:
                    states[ord(i)-97] = 2
                else:
                    continue
        
        for i in range(len(s)):
            if 65 <= ord(s[i]) <= 90:
                if states[ord(s[i]) - 65] == 1:
                    return i
            else:
                if states[ord(s[i]) - 97] == 1:
                    return i
        
        return -1