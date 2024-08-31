class TrieNode:
    
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.head = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.head
        for w in word:
            if w not in curr.children:
                curr.children[w] = TrieNode()
            curr = curr.children[w]
        
        curr.endOfWord = True

    def search(self, word: str) -> bool:

        def dfs(node, i):
            if i == len(word):
                return node.endOfWord
            
            if word[i] == '.':
                for child in node.children.values():
                    if dfs(child, i+1): return True
            if word[i] in node.children:
                    return dfs(node.children[word[i]], i+1)
            return False
        
        return dfs(self.head, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)