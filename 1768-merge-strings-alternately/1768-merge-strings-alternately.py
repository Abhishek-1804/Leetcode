class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        ans = ''
        w1, w2 = 0, 0

        for i in range(len(word1) + len(word2)):
            if i%2 == 0:
                if w1 < len(word1):
                    ans += word1[w1]
                    w1 += 1
                else:
                    break
            else:
                if w2 < len(word2):
                    ans += word2[w2]
                    w2 += 1
                else:
                    break

        if w1 < len(word1):
            ans += word1[w1:]

        if w2 < len(word2):
            ans += word2[w2:]
        
        return ans