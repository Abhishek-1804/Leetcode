# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not l1 or not l2:
            return l1 or l2

        dummy = head = ListNode(-1)

        carry = 0

        while l1 or l2:
            total = 0

            total += l1.val if l1 else 0
            if l1:
                l1 = l1.next

            total += l2.val if l2 else 0
            if l2:
                l2 = l2.next

            total += carry
            carry = 0

            head.next = ListNode(total%10)
            carry = total // 10
            head = head.next
        
        if carry:
            head.next = ListNode(1)
        
        return dummy.next
        