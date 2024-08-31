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
        stack = [(self.head, 0)]

        while stack:
            node, i = stack.pop()

            if i == len(word):
                if node.endOfWord:
                    return True
                continue

            if word[i] in node.children:
                stack.append((node.children[word[i]], i+1))
            elif word[i] == '.':
                for child in node.children.values():
                    stack.append((child, i+1))
        
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)