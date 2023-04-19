# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None
        ans=0
        def dfs(node,lvis,length):
            nonlocal ans
            if not node:
                return
            
            if lvis:
                dfs(node.right,False,length+1)
                dfs(node.left,True,1)
                ans=max(ans,length)
                
            if not lvis :
                dfs(node.left,True,length+1)
                dfs(node.right,False,1)
                ans=max(ans,length)
        
        dfs(root,True,0)
        dfs(root,False,0)
        return ans