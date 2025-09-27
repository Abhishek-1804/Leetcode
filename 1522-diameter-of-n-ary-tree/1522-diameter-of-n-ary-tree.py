"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """

        diameter = 0
        
        def dfs(node):

            nonlocal diameter

            if not node:
                return 0

            first_longest, second_longest = 0, 0
            if node.children:
                for child in node.children:
                    child_length = dfs(child)
                    if child_length > first_longest:
                        second_longest = first_longest
                        first_longest = dfs(child)
                    elif child_length > second_longest:
                        second_longest = dfs(child)
            
            diameter = max(diameter, first_longest + second_longest)

            return 1 + first_longest
        
        dfs(root)
        return diameter