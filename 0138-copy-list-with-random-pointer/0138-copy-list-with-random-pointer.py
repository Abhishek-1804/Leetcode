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
        
        dummy = Node(0)
        dummy.next = curr = head
        deep_copy = {None:None}

        while curr:
            deep_copy[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            deep_copy[curr].next = deep_copy[curr.next]
            deep_copy[curr].random = deep_copy[curr.random]
            curr = curr.next
        
        return deep_copy[head]
