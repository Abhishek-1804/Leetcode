class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        
        # Create a set for efficient similarity checking
        pairs = set()
        for a, b in similarPairs:
            pairs.add((a, b))
            pairs.add((b, a))  # similarity is generally bidirectional
        
        for w1, w2 in zip(sentence1, sentence2):
            # A word is always similar to itself
            if w1 == w2:
                continue
            if (w1, w2) not in pairs:
                return False
        return True
