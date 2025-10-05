class Solution:
    def countLetters(self, s: str) -> int:
        
        total = 0
        seen = set()
        n = len(s)

        for i in range(n):
            seen.add(s[i])
            for j in range(i, n):
                if s[j] in seen:
                    total += 1
                else:
                    break
            seen.pop()

        return total