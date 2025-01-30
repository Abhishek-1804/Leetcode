class Trie:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        dummy = Trie()
        head = dummy
        
        for l in strs[0]:
            head.children[l] = Trie()
            head = head.children[l]
        
        head.endOfWord = True
        ans = strs[0]

        for word in strs[1:]:
            length_ = 0
            head = dummy

            for l in word:
                if l not in head.children:
                    break
                head = head.children[l]
                length_ += 1
            
            if not length_:
                return ""
            
            ans = ans[:length_]
        
        return ans