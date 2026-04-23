# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.pre_order = []

        def traverse(root: Optional[TreeNode]):
            if not root:
                self.pre_order.append(None)
                return

            self.pre_order.append(root.val)
            traverse(root.left)
            traverse(root.right)

        traverse(p)
        traverse(q)

        n = len(self.pre_order)//2

        if self.pre_order[:n] == self.pre_order[n:]:
            return True
        else:
            return False

            

        