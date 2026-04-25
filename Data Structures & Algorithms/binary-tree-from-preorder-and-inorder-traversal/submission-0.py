# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        root = TreeNode(val=preorder[0])
        divide_pt = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1:divide_pt+1], inorder[:divide_pt]) #lst
        root.right = self.buildTree(preorder[divide_pt+1:], inorder[divide_pt+1:]) #rst

        return root



        
       
       
       
       
       
       
        #root, lst, bst [parts of inorder and preorder], preorder