#Initial Approach => 2-pass solution. Keep a counter to count total number of nodes in the first pass. Then in second pass move (count-n) nodes and remove the (count-n)nth node.
#Final Approach => 1-pass solution. Keep 2 pointers (first at head, second moved n-nodes ahead). Then move while loop till second exists. - This way second node is always n-nodes ahead of first.

#In both approaches we need a prev pointer.

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

