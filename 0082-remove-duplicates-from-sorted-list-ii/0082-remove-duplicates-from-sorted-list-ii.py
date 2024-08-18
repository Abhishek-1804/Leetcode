# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = curr = ListNode(-101)
        prev = curr.val
        dummy.next = head

        while head:
            if not head.next:
                if head.val == prev:
                    curr.next = None
                else:
                    curr.next = head

            elif head.val == prev or head.val == head.next.val:
                prev = head.val

            else:
                curr.next = head
                prev = head.val
                curr = curr.next

            head = head.next
        
        return dummy.next