# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return None
        q=[]
        q.append(root)
        nodeFound=False
        
        while q:
            node=q.pop(0)
            if not node:
                nodeFound=True
            else:
                if nodeFound:
                    return False
                q.append(node.left)
                q.append(node.right)
        return True