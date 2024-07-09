class TrieNode:
    
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(node, index):
            if index == len(word): 
                return node.endOfWord
            
            if word[index] == '.':
                for child in node.children.values():
                    if dfs(child, index+1):
                        return True

            if word[index] in node.children:
                return dfs(node.children[word[index]], index+1)
            
            return False
        
        return dfs(self.root, 0)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)