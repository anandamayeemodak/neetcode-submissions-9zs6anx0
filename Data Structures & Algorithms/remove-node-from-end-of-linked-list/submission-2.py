# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next:
            return

        first, second = head, head
        prev = None
        count = 0
        
        while count<n:
            second = second.next
            count += 1
        
        while second:
            prev = first
            first = first.next
            second = second.next

        if not prev:
            head = head.next
        else:
            prev.next = first.next

        return head

