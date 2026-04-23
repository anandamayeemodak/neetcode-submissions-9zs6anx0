"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head:
            return
            
        random_map = {}
        
        newHead = Node(head.val)
        cur = head.next
        newCur = newHead

        random_map[head] = newHead

        while cur:
            newNode = Node(cur.val)
            newCur.next = newNode
            random_map[cur] = newNode
            
            cur = cur.next
            newCur = newCur.next

        #Assigning random pointer
        cur = head
        newCur = newHead

        while cur:
            curRandom = cur.random
            newRandom = random_map[curRandom] if curRandom in random_map else None
            newCur.random = newRandom

            cur = cur.next
            newCur = newCur.next

        return newHead
        


        