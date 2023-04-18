# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans=[]
        q=[]
        if not root:
            return None
        q.append(root)
        while q:
            level = len(q)
            temp=[]
            for i in range(level):
                if q[0].left:
                    q.append(q[0].left)
                if q[0].right:
                    q.append(q[0].right)
                temp.append(q.pop(0).val)
            
            ans.append(temp)
        
        return ans