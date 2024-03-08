"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':

        # sol2
        def dfs(node):
            
            if not node:
                return None

            scanner = node.next

            while scanner:

                if scanner.left:
                    scanner = scanner.left
                    break
                
                if scanner.right:
                    scanner = scanner.right
                    break
                
                scanner = scanner.next
            
            if node.right:
                node.right.next = scanner
            
            if node.left:
                node.left.next = node.right if node.right else scanner
            
            dfs(node.right)
            dfs(node.left)

            return node
        
        return dfs(root)

        ## sol 1 bfs approach
        # if not root:
        #     return None
            
        # queue = [root]

        # while queue:
        #     size = len(queue)
            
        #     for i in range(size):
        #         node = queue.pop(0)
        #         if i < size - 1:
        #             node.next = queue[0]
                
        #         # Add children to the queue
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        
        # return root