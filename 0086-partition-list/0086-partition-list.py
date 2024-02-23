# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        dummyless = less = ListNode(-1)
        dummygreater = greater = ListNode(-1)

        curr = head
        while curr:
            if curr.val < x:
                less.next = curr
                less = less.next
                curr = curr.next
                less.next = None
            
            else:
                greater.next = curr
                greater = greater.next
                curr = curr.next
                greater.next = None

        curr = dummyless.next
        while curr:
            if not curr.next:
                curr.next = dummygreater.next
                break
            else:
                curr = curr.next
        
        return dummyless.next if dummyless.next else dummygreater.next