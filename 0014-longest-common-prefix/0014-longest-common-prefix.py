class Trie:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        dummy = Trie()
        head = dummy

        for c in strs[0]:
            head.children[c] = Trie()
            head = head.children[c]
        head.endOfWord = True

        ans = strs[0]

        for word in strs[1:]:
            head = dummy
            length_ = 0

            for c in word:
                if c not in head.children:
                    break
                head = head.children[c]
                length_ += 1
            
            if not length_:
                return ""
            ans = ans[:length_]
                
        return ans