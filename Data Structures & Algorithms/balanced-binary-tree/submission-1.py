# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def dfs(root: Optional[TreeNode]):
            if not root:
                return 0
            
            return 1 + max(dfs(root.left), dfs(root.right))

        
        leftH = dfs(root.left)
        rightH = dfs(root.right)

        diff = abs(leftH-rightH)
        if diff > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)


        