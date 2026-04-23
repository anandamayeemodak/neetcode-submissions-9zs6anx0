# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.tree_preOrder = []
        self.subtree_preOrder = []

        def traverse(root: Optional[TreeNode], tree_flag):
            if not root:
                if tree_flag:
                    self.tree_preOrder.append(None)
                else:
                    self.subtree_preOrder.append(None)
                return
            
            if tree_flag:
                    self.tree_preOrder.append(root.val)
            else:
                self.subtree_preOrder.append(root.val)

            traverse(root.left, tree_flag)
            traverse(root.right, tree_flag)

        traverse(root, True)
        traverse(subRoot, False)


        if len(self.tree_preOrder) == len(self.subtree_preOrder):
            return self.tree_preOrder == self.subtree_preOrder
        

        for i in range(len(self.tree_preOrder)-len(self.subtree_preOrder)+1):
            subTree = self.tree_preOrder[i:i+len(self.subtree_preOrder)]

            if subTree == self.subtree_preOrder:
                return True
        
        return False
        