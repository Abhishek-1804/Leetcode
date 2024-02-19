# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = jump = curr = ListNode(0)
        dummy.next = head

        for _ in range(n):
            jump = jump.next

        prev = None
        while jump:
            prev = curr
            curr = curr.next
            jump = jump.next

        prev.next = curr.next

        return dummy.next
