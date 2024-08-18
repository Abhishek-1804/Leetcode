# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        dummy_less = less_than = ListNode()
        dummy_greater = greater_than = ListNode()

        while head:
            if head.val < x:
                less_than.next = head
                less_than = less_than.next
            else:
                greater_than.next = head
                greater_than = greater_than.next
            
            head = head.next
        
        less_than.next = dummy_greater.next
        greater_than.next = None

        return dummy_less.next
