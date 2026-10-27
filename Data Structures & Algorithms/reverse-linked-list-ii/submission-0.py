# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        prev = dummy

        for i in range(1,left):
            prev = prev.next
        
        cur = prev.next

        for i in range(right-left):

            temp = prev.next
            prev.next = cur.next
            cur.next = cur.next.next
            prev.next.next = temp
        
        return dummy.next