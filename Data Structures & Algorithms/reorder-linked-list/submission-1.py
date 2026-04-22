# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        l1 = head

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        l2 = slow
        

        #reverse l2
        prev, cur = None, l2

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
            

        l2 = prev
        
        #merge lists
        cur1, cur2 = l1, l2
        while cur1.next and cur2.next:
            temp1, temp2 = cur1.next, cur2.next
            cur1.next = cur2
            cur2.next = temp1
            cur1, cur2 = temp1, temp2

        

            





        