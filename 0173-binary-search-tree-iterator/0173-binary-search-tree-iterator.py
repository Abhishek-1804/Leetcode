# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.ans = []
        self.dfs(root)
        self.iterator = -1  # Keeps track of the current position
    
    def dfs(self, node):
        """Perform in-order traversal and store the values."""
        if not node:
            return
        self.dfs(node.left)
        self.ans.append(node.val)
        self.dfs(node.right)

    def next(self) -> int:
        """Return the next smallest number."""
        self.iterator += 1
        return self.ans[self.iterator]

    def hasNext(self) -> bool:
        """Return whether we have a next smallest number."""
        return self.iterator + 1 < len(self.ans)  


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()