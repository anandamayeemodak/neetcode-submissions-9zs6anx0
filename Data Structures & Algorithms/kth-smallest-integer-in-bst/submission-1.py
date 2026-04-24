# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.max_heap = []

        def dfs(root):
            if not root:
                return
            if len(self.max_heap) < k:
                heapq.heappush_max(self.max_heap, root.val)
            else:
                heapq.heappushpop_max(self.max_heap, root.val)
            
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return self.max_heap[0]
            

        