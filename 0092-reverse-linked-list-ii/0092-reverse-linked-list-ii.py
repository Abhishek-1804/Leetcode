# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        dummy = ListNode()
        dummy.next = head

        counter = 1
        prev = None

        while head:
            if counter == left:
                break
            prev = head
            head = head.next
            counter += 1
        
        end = head
        temp = None

        while head:
            if counter == right+1:
                break
            nxt = head.next
            head.next = temp
            temp = head
            head = nxt
            counter += 1
        
        end.next = head
        
        if left == 1:
            return temp
        else:
            prev.next = temp
            return dummy.next