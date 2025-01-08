"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        h = {None:None}
        
        curr = head
        while curr:
            h[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            h[curr].next = h[curr.next]
            h[curr].random = h[curr.random]
            curr = curr.next
        
        return h[head]