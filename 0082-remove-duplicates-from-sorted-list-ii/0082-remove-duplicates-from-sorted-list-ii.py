# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = curr = ListNode(0)
        dummy.next = head

        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next

                head = head.next
            
            else:
                curr.next = head
                curr = curr.next
                head = head.next
        
        curr.next = None
        
        return dummy.next
