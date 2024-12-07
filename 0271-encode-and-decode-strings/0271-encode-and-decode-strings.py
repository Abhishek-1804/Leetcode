from typing import List

class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string."""
        # Prepend each string's length followed by a delimiter ':'
        return ''.join(f"{len(word)}:{word}" for word in strs)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings."""
        decoded = []
        i = 0
        while i < len(s):
            # Read the length part until the delimiter ':'
            j = s.find(':', i)
            length = int(s[i:j])  # Convert the length string to an integer
            # Extract the word of the specified length
            decoded.append(s[j + 1:j + 1 + length])
            # Move to the next encoded part
            i = j + 1 + length
        return decoded


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))