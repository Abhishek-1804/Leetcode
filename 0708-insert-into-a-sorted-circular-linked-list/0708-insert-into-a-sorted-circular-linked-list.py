"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        
        new_node = Node(insertVal)

        if not head:
            new_node.next = new_node
            return new_node

        curr = head

        while curr:
            # normal insert between two nodes
            if curr.val <= insertVal <= curr.next.val:
                break
            # handle wrap position (max -> min)
            if curr.val > curr.next.val and (insertVal >= curr.val or insertVal <= curr.next.val):
                break
            # full circle, insert anywhere
            if curr.next == head:
                break
            curr = curr.next

        new_node.next = curr.next
        curr.next = new_node
        return head