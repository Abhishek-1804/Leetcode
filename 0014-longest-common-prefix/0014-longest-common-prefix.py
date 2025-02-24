class Trie:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        dummy = head = Trie()

        for c in strs[0]:
            head.children[c] = Trie()
            head = head.children[c]
        
        head.endOfWord = True

        ans = strs[0]

        for word in strs[1:]:
            head = dummy
            temp_ans = ''
            for c in word:
                if c in head.children and not head.endOfWord:
                    head = head.children[c]
                    temp_ans += c
                else:
                    break
            
            head.endOfWord = True
            ans = temp_ans
        
        return ans