# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        bst=[]
        def inorder(node):
            if not node:
                return None
            
            inorder(node.left)
            bst.append(node.val)
            inorder(node.right)
        
        inorder(root)
        for i in range(1,len(bst)):
            if bst[i]<=bst[i-1]:
                return False
        return True
                
                