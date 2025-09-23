# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        
        curr = head

        while curr:
            # move forward m nodes
            for _ in range(m-1):
                if not curr:
                    return head
                curr = curr.next
            
            # delete n nodes
            temp = curr.next if curr else None 
            for _ in range(n):
                if temp is None:
                    break
                temp = temp.next
            
            if curr:
                curr.next = temp
                curr = temp
        
        return head