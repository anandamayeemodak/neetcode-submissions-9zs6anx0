# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        self.good_nodes = 0
        self.max_val = root.val

        def dfs(root, max_v):
            if not root:
                return None
            
            max_v = max(max_v, root.val)
            if max_v == root.val:
                self.good_nodes += 1
            
            dfs(root.left, max_v)
            dfs(root.right, max_v)

        dfs(root, self.max_val)
        return self.good_nodes

        