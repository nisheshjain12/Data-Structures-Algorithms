class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if not root:
            return False
        q=[]
        q.append(root)
        xP=None
        yP=None
        
        while q:
            level = len(q)
            for i in range(level):
                temp = q.pop(0)
                
                if temp.left:
                    q.append(temp.left)
                    
                    if temp.left.val == x:
                        xP=temp
                    if temp.left.val == y:
                        yP=temp
                        
                if temp.right:
                    q.append(temp.right)
                    
                    if temp.right.val == x:
                        xP=temp
                    if temp.right.val == y:
                        yP=temp
                
                if xP and yP:
                    if xP!=yP:
                        return True
                    else:
                        return False
                
            if (xP and yP==None) or (yP and xP==None):
                return False
            
        return False