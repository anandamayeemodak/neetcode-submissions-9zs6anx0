# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        if not l1 or not l2:
            return l1 or l2

        cur1 = l1
        cur2 = l2
        

        res = None
        cur_res = res
        carry = 0

        while cur1 or cur2:
            if not cur1:
                res_digit = cur2.val + carry
            elif not cur2:
                res_digit = cur1.val + carry
            else:         
                res_digit = cur1.val + cur2.val + carry

            if res_digit >= 10:
                carry = 1
                res_digit = res_digit - 10
            
            else:
                carry = 0
            
            res_node = ListNode(res_digit)
            if cur_res:
                cur_res.next = res_node
                cur_res = cur_res.next
        
            else:
                res = res_node
                cur_res = res

            cur1 = cur1.next if cur1 else None
            cur2 = cur2.next if cur2 else None
        
        if carry > 0:
            res_node = ListNode(carry)
            cur_res.next = res_node

        return res 




        