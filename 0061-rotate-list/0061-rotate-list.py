# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        dummy = ListNode(-1)
        dummy.next = head

        # calculating total length
        total_len = 0
        curr = head
        while curr:
            total_len += 1
            curr = curr.next

        # simplifying number of rotations
        num_rotations = k % total_len
        if num_rotations == 0:
            return head

        # creating a cycle
        curr = head
        while curr:
            if not curr.next:
                curr.next = head
                break

            else:
                curr = curr.next

        # breaking cycle at rotation
        curr = head
        count = 1
        while curr:
            if count == (total_len - num_rotations):
                dummy.next = curr.next
                curr.next = None
                return dummy.next

            else:
                count += 1
                curr = curr.next
