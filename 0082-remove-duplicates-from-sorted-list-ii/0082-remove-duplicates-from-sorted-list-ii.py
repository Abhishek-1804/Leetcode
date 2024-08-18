# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(-1)
        dummy.next = head

        curr = head
        prev = dummy

        while curr:
            # Check if the current node has a duplicate
            if curr.next and curr.val == curr.next.val:
                # Skip all nodes with the same value
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                # Link the previous node to the node after the last duplicate
                prev.next = curr.next
            else:
                # If no duplicate, just move the prev pointer to current
                prev = curr
            # Move current pointer forward in all cases
            curr = curr.next

        return dummy.next
