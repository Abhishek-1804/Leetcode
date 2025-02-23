# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = head = ListNode()
        carry = 0

        while l1 or l2 or carry:
            total_sum = 0

            if l1:
                total_sum += l1.val
                l1 = l1.next

            if l2:
                total_sum += l2.val
                l2 = l2.next
                
            total_sum += carry

            head.next = ListNode(total_sum%10)
            head = head.next
            carry = total_sum // 10
        
        return dummy.next