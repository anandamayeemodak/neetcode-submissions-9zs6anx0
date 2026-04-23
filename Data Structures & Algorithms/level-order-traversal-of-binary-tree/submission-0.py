# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        bfs = []

        while queue:
            level_len = len(queue)
            cur_level_nodes = []

            for _ in range(level_len):
                node = queue.popleft()
                cur_level_nodes.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            bfs.append(cur_level_nodes)
        
        return bfs

                

        