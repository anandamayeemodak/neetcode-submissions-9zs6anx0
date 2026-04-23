# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.d = 0

        if not root:
            return 0

        def dfs(root: Optional[TreeNode]):
            if not root:
                return 0
            
            return 1 + max(dfs(root.left), dfs(root.right))


        def diam(root: Optional[TreeNode]):
            if not root:
                 return 0

            leftH = dfs(root.left)
            rightH = dfs(root.right)

            self.d = max(self.d, (leftH + rightH), diam(root.left), diam(root.right))
            return self.d
        
        diam(root)
        
        return self.d
            

        