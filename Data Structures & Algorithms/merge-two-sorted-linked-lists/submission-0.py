# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or not list2:
            return list1 or list2
        
        newList = None
        cur1, cur2 = list1, list2

        if list1.val <= list2.val:
            newList = list1
            cur1 = cur1.next
        else:
            newList = list2
            cur2 = cur2.next

        newCur = newList

        while cur1 and cur2:
            if cur1.val <= cur2.val:
                newCur.next = cur1
                cur1 = cur1.next
            else:
                newCur.next = cur2
                cur2 = cur2.next
            
            newCur = newCur.next

        newCur.next = cur1 or cur2

        return newList


        
