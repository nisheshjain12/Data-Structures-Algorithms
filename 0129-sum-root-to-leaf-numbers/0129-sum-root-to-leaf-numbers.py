# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans=[]

        def trip(root,temp):
        
            temp.append(root.val)
            
            if not root.right and not root.left:
                ans.append(temp.copy())
                return 

            if root.left:
                trip(root.left,temp)
                temp.pop()
            if root.right:
                trip(root.right,temp)
                temp.pop()
        
        trip(root,[])

        sum=0
        
        for i in ans:
            num=0
            length=len(i)
            for j in range(length):
                num+=i[j]*(10**(length-j-1))
            sum+=num
        return sum









        
