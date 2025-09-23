# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        if not head:
            return ListNode(1)
        
        # Reverse the linked list
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        # Add one to the reversed list
        carry = 1
        curr = prev
        start = prev
        while curr and carry:
            curr.val += carry
            carry = curr.val // 10
            curr.val = curr.val % 10
            if not curr.next and carry:
                curr.next = ListNode(0)
            curr = curr.next

        # Reverse back to original order
        prev2 = None
        curr2 = start
        while curr2:
            nxt2 = curr2.next
            curr2.next = prev2
            prev2 = curr2
            curr2 = nxt2

        return prev2